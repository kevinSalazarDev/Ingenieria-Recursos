
$ErrorActionPreference = "Stop"

function Fail($message) {
    Write-Host ""
    Write-Host $message -ForegroundColor Red
    Write-Host "No se forzaron cambios ni se descartaron archivos." -ForegroundColor Yellow
    Read-Host "Presiona Enter para cerrar"
    exit 1
}

try {
    # Identificar el repositorio
    $repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
    Set-Location $repo

    if (-not (Test-Path (Join-Path $repo ".git"))) {
        Fail "No encuentro la carpeta .git."
    }

    $branch = (git branch --show-current).Trim()
    if ($LASTEXITCODE -ne 0 -or $branch -ne "main") {
        Fail "La rama actual no es main. No hice cambios."
    }

    Write-Host "====================================" -ForegroundColor Cyan
    Write-Host "       SINCRONIZADOR DE GITHUB" -ForegroundColor Cyan
    Write-Host "====================================" -ForegroundColor Cyan
    Write-Host "Repositorio: $repo"
    Write-Host "Rama: $branch"

    # Detectar operaciones Git pendientes
    $gitDir = (git rev-parse --git-dir).Trim()
    if ($LASTEXITCODE -ne 0) {
        Fail "No se pudo identificar la carpeta interna de Git."
    }

    $pendingOperations = @(
        "rebase-merge",
        "rebase-apply",
        "MERGE_HEAD",
        "CHERRY_PICK_HEAD",
        "REVERT_HEAD"
    )

    foreach ($operation in $pendingOperations) {
        if (Test-Path (Join-Path $gitDir $operation)) {
            Fail "Hay una operacion Git pendiente ($operation). Solicita ayuda antes de continuar."
        }
    }

    # No continuar si existen cambios preparados previamente
    $staged = git diff --cached --name-only
    if ($LASTEXITCODE -ne 0) {
        Fail "No se pudo revisar el area de preparacion."
    }

    if ($staged) {
        Write-Host "Hay cambios preparados previamente." -ForegroundColor Yellow
        Write-Host "No los modificare ni incluire automaticamente."
        Fail "Revisa los cambios preparados antes de sincronizar."
    }

    # Consultar GitHub
    Write-Host ""
    Write-Host "Consultando GitHub..." -ForegroundColor Cyan

    git fetch origin
    if ($LASTEXITCODE -ne 0) {
        Fail "No se pudo consultar GitHub. Revisa tu conexion."
    }

    # Mostrar cambios locales
    Write-Host ""
    Write-Host "ESTADO ACTUAL:" -ForegroundColor Cyan
    git status -sb
    if ($LASTEXITCODE -ne 0) {
        Fail "No se pudo revisar el estado."
    }

    Write-Host ""
    Write-Host "CAMBIOS LOCALES:" -ForegroundColor Cyan
    git status --short

    Write-Host ""
    Write-Host "ATENCION:"
    Write-Host "Se pueden incluir archivos nuevos, modificados y eliminados."
    Write-Host "Revisa que no existan contrasenas, claves ni archivos privados."

    $answer = Read-Host "¿Deseas preparar todos los cambios locales? (S/N)"
    if ($answer -notmatch '^(s|si|sí)$') {
        Write-Host "Cancelado. No se modificaron archivos." -ForegroundColor Yellow
        Read-Host "Presiona Enter para cerrar"
        exit 0
    }

    # Preparar los cambios
    git add -A
    if ($LASTEXITCODE -ne 0) {
        Fail "No se pudieron preparar los archivos."
    }

    git diff --cached --quiet
    $diffResult = $LASTEXITCODE

    if ($diffResult -eq 1) {
        Write-Host ""
        Write-Host "CAMBIOS QUE SE GUARDARAN:" -ForegroundColor Cyan
        git diff --cached --name-status

        $confirm = Read-Host "¿Confirmas crear un commit con estos cambios? (S/N)"
        if ($confirm -notmatch '^(s|si|sí)$') {
            git reset
            if ($LASTEXITCODE -ne 0) {
                Fail "No se pudieron retirar los cambios del area de preparacion. Tus archivos siguen intactos."
            }
            Write-Host "Cancelado. Los archivos originales siguen intactos." -ForegroundColor Yellow
            Read-Host "Presiona Enter para cerrar"
            exit 0
        }

        $message = "Actualizacion del repositorio: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        git commit -m $message
        if ($LASTEXITCODE -ne 0) {
            Fail "No se pudo crear el commit. Tus archivos siguen en el repositorio."
        }
    }
    elseif ($diffResult -eq 0) {
        Write-Host "No hay cambios locales nuevos para guardar." -ForegroundColor Green
    }
    else {
        Fail "No se pudo comprobar si existen cambios preparados."
    }

    # Comprobar divergencia con GitHub
    Write-Host ""
    Write-Host "Comprobando diferencias con GitHub..." -ForegroundColor Cyan

    $counts = git rev-list --left-right --count main...origin/main
    if ($LASTEXITCODE -ne 0) {
        Fail "No se pudieron comparar las ramas."
    }

    $parts = $counts.Trim() -split '\s+'
    $ahead = [int]$parts[0]
    $behind = [int]$parts[1]

    Write-Host "Commits locales pendientes de subir: $ahead"
    Write-Host "Commits remotos pendientes de integrar: $behind"

    if ($ahead -gt 0 -and $behind -gt 0) {
        Fail "Las ramas tienen cambios diferentes. Se necesita revisar la integracion manualmente."
    }

    if ($behind -gt 0 -and $ahead -eq 0) {
        Write-Host "Actualizando mediante avance seguro..." -ForegroundColor Cyan
        git merge --ff-only origin/main
        if ($LASTEXITCODE -ne 0) {
            Fail "No se pudo actualizar mediante avance seguro."
        }
    }

    if ($ahead -gt 0) {
        Write-Host ""
        Write-Host "Subiendo cambios a GitHub..." -ForegroundColor Cyan
        git push origin main
        if ($LASTEXITCODE -ne 0) {
            Fail "No se pudo subir. Tus commits locales se conservaron."
        }
    }
    else {
        Write-Host "No hay commits locales pendientes de subir." -ForegroundColor Green
    }

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
