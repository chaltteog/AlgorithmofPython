@echo off

REM===================================
SET REPOSITORY=.\.git\refs
REM===================================

SET REPOSITORY_HEADS=.\.git\refs\heads
SET REPOSITORY_REMOTES=.\.git\refs\remotes\origin

SET REPOSITORY_HEADS_CMD=dir %REPOSITORY_HEADS% /b
SET REPOSITORY_REMOTES_CMD=dir %REPOSITORY_REMOTES% /b


git checkout master

for /F "tokens=*" %%F in ('%REPOSITORY_HEADS_CMD%') do (
    if not "%%F"=="master" if not "%%F"=="alpha" if not "%%F"=="beta" (
        del /q %REPOSITORY_HEADS%\%%F
    )
)

for /F "delims= tokens=*" %%F in ('%REPOSITORY_REMOTES_CMD%') do (
    if not "%%F"=="master" if not "%%F"=="alpha" if not "%%F"=="beta" (
        del /q %REPOSITORY_REMOTES%\%%F
    )
)

git pull