## 0x11-python-network_1
### Python Network Scripting

This repository contains Python scripts for network-related tasks, including making HTTP requests, handling responses, and interacting with APIs.

## Contents

1. [0-hbtn_status.py](#0-hbtn_statuspy)
2. [1-hbtn_header.py](#1-hbtn_headerpy)
3. [2-post_email.py](#2-post_emailpy)
4. [3-error_code.py](#3-error_codepy)
5. [4-hbtn_status.py](#4-hbtn_statuspy)
6. [5-hbtn_header.py](#5-hbtn_headerpy)
7. [6-post_email.py](#6-post_emailpy)
8. [7-error_code.py](#7-error_codepy)
9. [8-json_api.py](#8-json_apipy)
10. [10-my_github.py](#10-my_githubpy)
11. [100-github_commits.py](#100-github_commitspy)

## Contents Description

### 0-hbtn_status.py

- Fetches the status of a URL using urllib.

### 1-hbtn_header.py

- Sends a request to a URL and displays the value of the `X-Request-Id` variable in the response header using urllib.

### 2-post_email.py

- Sends a POST request to a URL with an email parameter and displays the body of the response using urllib.

### 3-error_code.py

- Sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code.

### 4-hbtn_status.py

- Fetches the status of a URL using the `requests` package.

### 5-hbtn_header.py

- Sends a request to a URL and displays the value of the `X-Request-Id` variable in the response header using the `requests` package.

### 6-post_email.py

- Sends a POST request to a URL with an email parameter and displays the body of the response using the `requests` package.

### 7-error_code.py

- Sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code using the `requests` package.

### 8-json_api.py

- Sends a POST request to a URL with a letter parameter and displays the body of the response. If the response is JSON formatted and not empty, it displays the id and name. Otherwise, it prints appropriate messages.

### 10-my_github.py

- Uses Basic Authentication with a personal access token to access GitHub API and display the user id.

### 100-github_commits.py

- Lists the 10 most recent commits of a repository by a user using the GitHub API. It takes the repository name and owner name as command-line arguments.
