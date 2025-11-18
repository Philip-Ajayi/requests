import socket
import ssl

# Server info
HOST = "tptrans.lynksystems.com"
PORT = 6661

# Your CA certificate file
CA_CERT = "ca_root.pem"   # Change to your actual file

# Raw payload (must be bytes)
payload = (
    "BT00610000000000000004D412E08008220000000000000040000000000000005011304270000050001"
)

def main():
    # Build SSL context with your CA
    context = ssl.create_default_context(cafile=CA_CERT)

    # OPTIONAL: force TLSv1.2 if required
    # context.minimum_version = ssl.TLSVersion.TLSv1_2

    # Create TCP socket
    with socket.create_connection((HOST, PORT)) as sock:
        # Wrap socket in SSL
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            print("Connected with cipher:", ssock.cipher())

            # Send data
            ssock.sendall(payload.encode("ascii"))
            print("Payload sent.")

            # Receive response (if host sends one)
            response = ssock.recv(4096)
            print("Response:")
            print(response.decode(errors="ignore"))

if __name__ == "__main__":
    main()
