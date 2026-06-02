import subprocess

def unsafe_run(user_input):
    print("[UNSAFE] Running with shell=True:")
    result = subprocess.run(f"echo {user_input}", shell=True, capture_output=True, text=True)
    print(result.stdout)

def safe_run(user_input): 
    print("[SAFE] Running with shell=False:")
    result = subprocess.run(["echo", user_input], capture_output=True, text=True)
    print(result.stdout)

print("=== Normal input ===")
unsafe_run("hello")
safe_run("hello")


print("=== Malicious input ===")
unsafe_run("hello ; echo INJECTED!")
safe_run("hello ; echo INJECTED!")