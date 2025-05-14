# oapi-client-template

Please also refer to the [oapi documentation](https://oapi.enorganic.org/) for
detailed usage information.

To create a repository based on this template:

-   Execute the following commands (replacing "~/Code" with the path under
    which you want to create your new project):

    ```bash
    pip3 install --upgrade pip && \
    pip3 install cookiecutter && \
    cd ~/Code && \
    cookiecutter "https://github.com/enorganic/oapi-client-template.git"
    ```

-   Follow the prompts to enter template fields. For example:

    ```console
    $ cookiecutter "https://github.com/enorganic/oapi-client-template.git"

    ...
    ```

    The resulting directory/file structure created by the above example input
    looks as follows:

    ```console
    $ tree -a -I 'venv|.git|.mypy_cache|*.egg-info' oapi-test-client
    oapi-client-test-project
    ├── .editorconfig
    ├── .github
    │   └── workflows
    │       ├── distribute.yml
    │       └── test.yml
    ├── .gitignore
    ├── Makefile
    ├── README.md
    ├── oapi-client-test-project
    │   ├── __init__.py
    │   ├── client.py
    │   ├── model.py
    │   └── py.typed
    ├── pyproject.toml
    └── tests
       ├── conftest.py
       └── test_integration.py
    ```

-   Once you've created your new project, you will want to start by
    editing `scripts/remodel.py` (read the inline comments for instruction).
    Once you've edited this as needed, run
    `cd oapi-client-test-project && make remodel` to generate
    your model and client modules.

-   Edit `tests/conftest.py` such that `get_client` returns a client
    connecting to a suitable instance of the API against which to perform
    integration tests.

-   Author your integration tests in `tests/test_integration.py`
    (read inline comments for instruction).

-   Run `make test` to execute your tests. When/if validation errors are
    raised for API responses, edit the `fix_openapi` function in
    `scripts/remodel.py` to fix the OpenAPI document such that it correctly
    represents the data returned. For perfect Open API documents, this
    step will not be necessary, but candidly I've found precious few *perfect*
    Open API documents in the wild :-).

-   You will first need to create your repository on Github:
    `https://github.com/organizations/your-organization/repositories/new`
    (replace "your-organization" with your organization, of course)

-   Initialize and configure your repository locally. For the project created
    in our preceding examples, those commands would be:

    ```bash
    git init && \
    git add . && \
    git stage . && \
    git commit -m "First Commit" && \
    git remote add origin "https://github.com/your-organization/oapi-client-test-project.git"
    ```
