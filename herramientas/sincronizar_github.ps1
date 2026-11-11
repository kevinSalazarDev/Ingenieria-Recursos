$ErrorActionPreference = "Stop"

function Fail($message) {
    Write-Host ""
    Write-Host $message -ForegroundColor Red
    Write-Host "No se forzo ningun cambio ni se uso force push." -ForegroundColor Yellow
    Read-Host "Presiona Enter para cerrar"
    exit 1
}

try {
    $repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
    Set-Location $repo

    if (-not (Test-Path (Join-Path $repo ".git"))) {
        Fail "No encuentro la carpeta .git. Coloca estos dos archivos dentro de Ingenieria-Recursos."
    }

    $branch = (git branch --show-current).Trim()
    if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
        Fail "La rama actual no es main (detectada: '$branch'). No hice cambios."
    }

    Write-Host "Repositorio: $repo" -ForegroundColor Cyan
    Write-Host "Rama: main"
    Write-Host ""
    Write-Host "Revisando GitHub..." -ForegroundColor Cyan
    git fetch origin
    if ($LASTEXITCODE -ne 0) { Fail "No se pudo conectar con GitHub. Revisa tu conexion." }

    Write-Host ""
    Write-Host "Cambios locales detectados:" -ForegroundColor Cyan
    git status --short
    if ($LASTEXITCODE -ne 0) { Fail "No se pudo revisar el estado del repositorio." }

    Write-Host ""
    Write-Host "ATENCION: se incluiran los archivos nuevos, modificados y eliminados del repositorio."
    Write-Host "Asegurate de no tener contrasenas, claves ni archivos privados dentro del proyecto."
    $answer = Read-Host "¿Deseas sincronizar estos cambios con GitHub? (S/N)"
    if ($answer -notmatch '^(s|si|sí)$') {
        Write-Host "Cancelado. No se modifico nada." -ForegroundColor Yellow
        Read-Host "Presiona Enter para cerrar"
        exit 0
    }

    git add -A
    if ($LASTEXITCODE -ne 0) { Fail "No se pudieron preparar los archivos." }

    git diff --cached --quiet
    $hasChanges = ($LASTEXITCODE -ne 0)

    if ($hasChanges) {
        $message = "Actualizacion del repositorio: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        git commit -m $message
        if ($LASTEXITCODE -ne 0) { Fail "No se pudo crear el commit. Revisa la configuracion de Git." }
    } else {
        Write-Host "No hay cambios locales nuevos para guardar." -ForegroundColor Green
    }

    Write-Host ""
    Write-Host "Integrando cambios de GitHub..." -ForegroundColor Cyan
    git pull --rebase origin main
    if ($LASTEXITCODE -ne 0) {
        Fail "La integracion no termino. Puede haber un conflicto. No se subio nada; conserva esta ventana y pide ayuda antes de continuar."
    }

    Write-Host ""
    Write-Host "Subiendo a GitHub..." -ForegroundColor Cyan
    git push origin main
    if ($LASTEXITCODE -ne 0) { Fail "No se pudo subir a GitHub. Tus cambios locales siguen en el repositorio." }

    Write-Host ""
    Write-Host "SINCRONIZACION COMPLETADA." -ForegroundColor Green
    git status -sb
    Read-Host "Presiona Enter para cerrar"
}
catch {
    Write-Host ""
    Write-Host ("Error: " + $_.Exception.Message) -ForegroundColor Red
    Read-Host "Presiona Enter para cerrar"
    exit 1
}
