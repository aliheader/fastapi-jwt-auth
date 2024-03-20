# FastAPI JWT Authentication

This repository provides a simple implementation of JWT (JSON Web Tokens) authentication in FastAPI.

## Features

- User authentication using JWT tokens
- Token generation endpoint
- Basic error handling
- Scalable and extensible architecture

## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Python-Jose](https://python-jose.readthedocs.io/en/latest/)
- [uvicorn](https://www.uvicorn.org/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/fastapi-jwt-auth.git
    ```

2. Navigate into the cloned directory:

    ```bash
    cd fastapi-jwt-auth
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the token generation endpoint:

    Open your web browser or use a tool like [Postman](https://www.postman.com/) to send a POST request to `http://localhost:8000/api/auth/access-token`. Include the username and password in the body (form-data) to receive a JWT token in response.

## Configuration

- You can configure the JWT secret key, token expiration time, and other settings in the `config.py` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
