from alembic.config import Config
from alembic import command

#Helper function for migration
def main():
    alembic_cfg = Config("../alembic.ini")
    command.revision(alembic_cfg, message="new action")
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    main()