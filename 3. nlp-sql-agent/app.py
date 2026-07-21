import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_groq import ChatGroq

# Shared API key lives in a single .env at the repo root, one level up from this project
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

MODEL_ID = "llama-3.3-70b-versatile"


def build_agent():
    llm = ChatGroq(
        model=MODEL_ID,
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2,
    )

    mysql_username = os.getenv("MYSQL_USERNAME", "root")
    mysql_password = os.getenv("MYSQL_PASSWORD", "")
    mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
    mysql_port = os.getenv("MYSQL_PORT", "3306")
    database_name = os.getenv("MYSQL_DATABASE", "Chinook")

    mysql_uri = (
        f"mysql+mysqlconnector://{mysql_username}:{mysql_password}"
        f"@{mysql_host}:{mysql_port}/{database_name}"
    )
    db = SQLDatabase.from_uri(mysql_uri)

    return create_sql_agent(
        llm=llm,
        db=db,
        verbose=True,
        handle_parsing_errors=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )


def main():
    parser = argparse.ArgumentParser(description="Ask a natural-language question about the connected MySQL database")
    parser.add_argument("--prompt", type=str, required=True, help="The natural-language question to send to the SQL agent")
    args = parser.parse_args()

    agent_executor = build_agent()
    result = agent_executor.invoke(args.prompt)
    print("\nAnswer:", result.get("output", result))


if __name__ == "__main__":
    main()
