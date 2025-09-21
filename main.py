import subprocess

def get_sshx_link():
    try:
        # Run sshx and capture the first line (the link)
        result = subprocess.run(
            ["sshx"],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.strip()
        # sshx prints instructions and link, so we just find the line with https
        for line in output.splitlines():
            if line.startswith("https://"):
                return line
        return None
    except subprocess.CalledProcessError as e:
        print("Error while running sshx:", e)
        return None

if __name__ == "__main__":
    link = get_sshx_link()
    if link:
        print("🔗 Your sshx link:", link)
    else:
        print("❌ Failed to get sshx link")
