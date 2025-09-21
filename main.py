import subprocess

def get_sshx_link():
    try:
        # Run sshx command and capture output
        result = subprocess.run(
            ["curl", "-sSf", "https://sshx.io/get"],
            capture_output=True,
            text=True,
            check=True
        )
        link = result.stdout.strip()
        return link
    except subprocess.CalledProcessError as e:
        print("Error while fetching sshx link:", e)
        return None

if __name__ == "__main__":
    link = get_sshx_link()
    if link:
        print("🔗 Your sshx link:", link)
    else:
        print("❌ Failed to get sshx link")
