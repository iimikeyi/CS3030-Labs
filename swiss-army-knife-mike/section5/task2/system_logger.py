import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s"
)

def main():
    logging.info("Script started")
    logging.warning("Low disk space")
    logging.error("Database connection failed")
    logging.info("Script finished")

if __name__ == "__main__":
    main()
