# Dev Container for Python and React

This repository offers a development environment set up with Docker, specifically designed for projects that use both Python and React. It takes advantage of Visual Studio Code's Dev Containers feature to provide a consistent and isolated workspace.

## Features

- **Isolated Development Environment**: Use Docker to create a uniform workspace, removing any discrepancies in the environment.
- **Pre-configured Services**: Ready for both Python and React development, making the setup process smoother.
- **VS Code Integration**: Effortless integration with Visual Studio Code's Dev Containers for an improved development experience.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Perpetue237/devcontainerPythonReact.git
   cd devcontainerPythonReact
   ```

2. **Open in VS Code**:

   Make sure you have the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed. Open the repository in VS Code and, when prompted, reopen it in the container.

3. **Start Services**:

   - Start the frontend with:
     ```bash
     cd frontend
     npm run dev
     ```
   - Start the backend with:
     ```bash
     cd backend
     uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
     ```

4. **Start Developing**:

   Now that your environment is set up, you can start developing your Python and React applications without any hassle.

## Requirements

- [Docker](https://www.docker.com/get-started) must be installed on your machine.
- [Visual Studio Code](https://code.visualstudio.com/) along with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

## Additional Resources
I have published a detailed video on my YouTube channel explaining how to use this repository and the concepts behind it. Watch it now [here](https://youtu.be/Y94p1PU9hBo)!
## License

This project is licensed under the Apache License 2.0. For more details, see the [LICENSE](LICENSE) file.
