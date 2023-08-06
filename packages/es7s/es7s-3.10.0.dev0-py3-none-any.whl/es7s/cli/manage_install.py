# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2021-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import os
import shutil

import pkg_resources

from ._decorators import cli_pass_context, _catch_and_log_and_exit, cli_option, cli_command
from .. import APP_NAME
from ..shared import get_logger, get_stdout
from ..shared.path import RESOURCE_DIR, USER_ES7S_BIN_DIR


@cli_command(__file__)
@cli_option(
    "-n",
    "--dry-run",
    is_flag=True,
    default=False,
    help="Don't actually do anything, just pretend to.",
)
@cli_option(
    "-s",
    "--symlinks",
    is_flag=True,
    default=False,
    help="Make symlinks to core files instead of copying them. "
    "Useful for es7s development, otherwise unnecessary.",
)
@_catch_and_log_and_exit
class InstallCommand:
    """Install es7s system."""

    def __init__(self, dry_run: bool, symlinks: bool, **kwargs):
        self._dry_run = dry_run
        self._symlinks = symlinks
        self._run()

    def _run(self):
        self._run_prepare()
        self._run_copy_core()
        self._run_inject_bashrc()
        self._run_inject_gitconfig()
        self._run_copy_bin()
        self._run_install_with_apt()
        self._run_install_with_pip()
        self._run_install_x11()
        self._run_dload_install()
        self._run_build_install_tmux()
        self._run_build_install_less()
        self._run_install_es7s_exts()
        self._run_install_daemon()
        self._run_install_shocks_service()
        #self._run_setup_cron()

    def _run_prepare(self):
        # install docker
        # sudo xargs -n1 <<< "docker syslog adm sudo" adduser $(id -nu)
        # ln -s /usr/bin/python3 ~/.local/bin/python
        pass

    def _run_copy_core(self):
        # install i -cp -v
        # git+ssh://git@github.com/delameter/pytermor@2.1.0-dev9
        pass

    def _run_inject_bashrc(self):
        pass

    def _run_inject_gitconfig(self):
        pass

    def _run_copy_bin(self):
        logger = get_logger()

        def _remove_obsolete(user_path: str) -> bool:
            msg = "Removing obsolete file: %s" % user_path
            if self._dry_run:
                logger.info(f"[DRY-RUN] {msg}")
                return True
            try:
                logger.info(msg)
                os.unlink(user_path)
            except Exception as e:
                logger.exception(e)
                return False
            return not os.path.exists(user_path)

        def _copy_to_bin(dist_path: str, user_path: str) -> bool:
            msg = "%s: %s" % ("Linking" if self._symlinks else "Copying", user_path)
            if self._dry_run:
                logger.info(f"[DRY-RUN] {msg}")
                return True
            try:
                if self._symlinks:
                    os.symlink(dist_path, user_path)
                    logger.info(f"Linked: {dist_path} -> {user_path}")
                else:
                    shutil.copy(dist_path, user_path)
                    logger.info(f"Copied: {dist_path} -> {user_path}")
            except Exception as e:
                logger.exception(e)
                return False
            return True

        successful = 0

        dist_dir_relpath = os.path.join(RESOURCE_DIR, "bin")
        dist_dir = pkg_resources.resource_listdir(APP_NAME, dist_dir_relpath)
        for dist_relpath in dist_dir:
            dist_abspath = pkg_resources.resource_filename(
                APP_NAME, os.path.join(dist_dir_relpath, dist_relpath)
            )
            user_abspath = os.path.join(USER_ES7S_BIN_DIR, os.path.basename(dist_relpath))
            if os.path.exists(user_abspath):
                if not _remove_obsolete(user_abspath):
                    logger.warning(f"Failed to remove file: '{user_abspath}', skipping...")
                    continue
            if not _copy_to_bin(dist_abspath, user_abspath):
                raise RuntimeError(f"Failed to copy file, aborting", [dist_abspath])
            successful += 1

        get_stdout().echo(f"Success for {successful}/{len(dist_dir)} files")

    def _run_install_with_apt(self):
        pass

    def _run_install_with_pip(self):
        pass

    def _run_install_x11(self):
        pass

    def _run_dload_install(self):
        # ginstall exa
        # ginstall bat
        pass

    def _run_build_install_tmux(self):
        # install tmux deps
        # build_tmux
        # ln -s `pwd`/tmux ~/bin/es7s/tmux
        # git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
        # tmux run-shell /home/delameter/.tmux/plugins/tpm/bindings/install_plugins
        pass

    def _run_build_install_less(self):
        # install less deps
        # build_less
        pass

    def _run_install_es7s_exts(self):
        # install i -i -v

        # colors
        # fonts?
        # > pipx install kolombos
        # leo
        # > pipx install macedon
        # watson
        # nalog
        pass

    def _run_install_daemon(self):
        # copy es7s.service to /etc/systemd/system
        # replace USER placeholders
        # enable es7s, reload systemd
        pass

    def _run_install_shocks_service(self):
        # copy es7s-shocks.service to /etc/systemd/system
        # replace USER placeholders
        # enable shocks, reload systemd
        pass
