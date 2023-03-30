from subprocess import run, PIPE

# Install the required packages from Git
run(["pip3", "install", "git+https://github.com/tomquirk/linkedin-api.git"])
run(["pip3", "install", "linkedin-api~=2.0.0a"])
