# Data Models
![Alt text](schema.png)

1. User
    - This table will store user information
2. Portfolio
    - This table will store portfolio information
    - Currently, it doesn't add much value, but allows for extensibility, such as allowing a user to create multiple portfolios
3. CurrencyAllocation
    - This table will store the cryptocurrencies associated with a particular portfolio
4. Currency
    - This table stores all available currencies in the system
    - This should be mostly static data (name, symbol, etc.)
5. CurrencySnapshot
    - This table stores market data for all currencies. 
    - It will contain one row for each currency
    - This table will be updated daily with the latest market data.

# Project Structure
- project/
    - Django App
- ui/
    - React App
- docker-compose.yml
    - Used for spinning up local resources for development
    - Redis (Celery Broker)
    - Celery Beat
    - Celery Worker
    - Postgres
- Dockerfile.celery
    - Dockerfile that defines the container for celery beat and worker processes to run in

# Crypto Data
Crypto market data gathered via coingecko's public API (https://api.coingecko.com/api)

# Improvements
1. Standardized validation/serialization
2. Standardized exception handling / response messages
3. Client is not organized at all, focus was on django backend
    - Should use some form of state management (context, redux, etc.)
    - Should centralize API calls into services
    - Should do actual routing between pages (react-router)
4. AuthN/AuthZ