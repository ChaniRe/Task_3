import docker
# Connecting to Docker engine
client = docker.from_env()

# Start a 'busybox' container in the background (detach=True)
container = client.containers.run(
    image="busybox",
    command=["sleep", "3000"],
    detach=True
)
# Run an additional command ('hostname') inside the already running container
exec_result = container.exec_run("hostname")
hostname = exec_result.output.decode().strip()
print("Container hostname:", hostname)
container.stop()
container.remove()
