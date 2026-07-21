# NLP SQL Agent

Natural-language-to-SQL agent that lets you ask plain-English questions about a MySQL database and get back an answer, using an LLM to reason about the schema and write/execute the SQL itself.

## Overview

NLP SQL Agent connects a LangChain SQL agent to a MySQL database and a Groq-hosted LLM. Given a question like "Which genre has the most tracks?", the agent:

- Lists the available tables
- Inspects the schema of the tables it thinks are relevant
- Writes a SQL query, double-checks it, then executes it
- Returns a plain-English answer based on the query result

It ships with the [Chinook sample database](https://github.com/lerocha/chinook-database) (a small digital media store schema: artists, albums, tracks, customers, invoices, etc.) so it works out of the box, but it will happily connect to any MySQL database.

## Technology Stack

- **Python 3.9+**
- **LangChain** / **langchain-community** - SQL agent framework
- **langchain-groq** - Groq LLM integration
- **Groq** - LLM inference (`llama-3.3-70b-versatile`)
- **MySQL** - target database
- **python-dotenv** - environment variable management

## Prerequisites

- Python 3.9 or higher
- A running MySQL server (local install is fine)
- Groq API access (free tier available at [console.groq.com](https://console.groq.com))

## Installation

### 1. Clone or Download

```bash
git clone <repository-url>
cd "3. nlp-sql-agent"
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Load the bundled Chinook sample database into your local MySQL server:

```bash
mysql -u root -h 127.0.0.1 < chinook-mysql.sql
```

This drops and recreates a `Chinook` database. Point `MYSQL_DATABASE` at a different database if you'd rather query your own data — the agent works against any schema.

### 5. Configure Environment Variables

This project shares a single `.env` file with the rest of the portfolio, located in the repo root (one level up from this folder, i.e. `../.env`). Copy the template and fill in your key:

```bash
cp ../.env.example ../.env
```

```
GROQ_API_KEY=your_api_key_here
MYSQL_USERNAME=root
MYSQL_PASSWORD=
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=Chinook
```

Get a free API key at [console.groq.com](https://console.groq.com). The MySQL variables default to a local, passwordless `root` install if left unset.

## Usage

```bash
python app.py --prompt "How many artists are in the database?"
python app.py --prompt "Which genre has the most tracks?"
python app.py --prompt "List the top 5 customers by total invoice amount"
```

The agent prints its reasoning trace (tables checked, schema inspected, SQL written and validated, query executed) followed by a final plain-English answer.

## Project Structure

```
.
├── app.py               # Agent setup and CLI entry point
├── chinook-mysql.sql    # Sample database schema + data
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variable template (see root .env.example)
```

## How It Works

1. **Connection**: `SQLDatabase.from_uri` connects to the target MySQL database using credentials from the environment
2. **Agent Setup**: `create_sql_agent` wires a Groq-backed LLM to a zero-shot ReAct agent with SQL tools (list tables, get schema, check query, run query)
3. **Reasoning Loop**: given a natural-language prompt, the agent decides which tables are relevant, inspects their schema, drafts a SQL query, validates it, then executes it
4. **Answer**: the query result is turned into a final natural-language answer

## Troubleshooting

**Import Errors**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Can't Connect to MySQL**
```bash
# Make sure the server is running
brew services start mysql   # macOS/Homebrew

# Verify credentials
mysql -u root -h 127.0.0.1 -e "SHOW DATABASES;"
```

**API Key Errors**
```bash
# Verify .env exists in the repo root and contains a valid GROQ_API_KEY
cat ../.env
```

## License

This project is provided as-is for educational and research purposes. The bundled Chinook database is licensed separately — see [chinook-database](https://github.com/lerocha/chinook-database/blob/master/LICENSE.md).

## Author

Developed by Anas AlGhannam

## Acknowledgments

- Groq for LLM inference
- LangChain for the SQL agent framework
- Luis Rocha for the Chinook sample database
