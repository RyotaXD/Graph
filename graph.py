import requests
import uuid
import hashlib
import random
import json


class MetaBusiness:
	def __init__(self):
		self.devices = [
			{"model": "SM-S928B", "ver": "14", "den": "3.0", "res": "1080x2340"},
			{"model": "Pixel 8 Pro", "ver": "14", "den": "3.5", "res": "1344x2992"},
			{"model": "Xiaomi 14 Ultra", "ver": "14", "den": "3.0", "res": "1440x3200"}
		]
		self.api_key = '121876164619130'
		self.token = '121876164619130|1ab2c5c902faedd339c14b2d58e929dc'

	def get_random_assets(self):
		dev = random.choice(self.devices)
		fbav = "450.0.0.45.109"
		fbbv = "612948572"
		ua = f"[FBAN/MBSA;FBLC/id_ID;FBAV/{fbav};FBBV/{fbbv};FBCR/Indosat;FBMF/Samsung;FBBD/Samsung;FBDV/{dev['model']};FBSV/{dev['ver']};FBCA/arm64-v8a:armeabi-v7a;FBDM/{{density={dev['den']},width={dev['res'].split('x')[0]},height={dev['res'].split('x')[1]}}};FB_FW/1;]"
		return ua

	def generate_sig(self, params):
		app_secret = "62f8ce9f74b12f84c123cc23462f4e56"
		sorted_params = "".join(f"{k}={v}" for k, v in sorted(params.items()))
		return hashlib.md5((sorted_params + app_secret).encode("utf-8")).hexdigest()

	def login_request(self, user, password):
		dev_id = str(uuid.uuid4())
		useragent = self.get_random_assets()
		headers = {
			'Host': 'b-graph.facebook.com',
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded',
			'User-Agent': useragent,
			'Authorization': 'OAuth null',
			'X-FB-Friendly-Name': 'authenticate',
			'X-FB-HTTP-Engine': 'Tigon/Liger',
			'X-FB-Connection-Type': 'WIFI',
			'X-FB-Connection-Quality': 'GOOD',
			'X-FB-Request-Analytics-Tags': json.dumps({"network_tags":{"product":self.api_key,"retry_attempt":"0"},"application_tags":"unknown"}),
			'X-FB-Net-HNI': str(random.randint(47000, 47999)),
			'X-FB-SIM-HNI': str(random.randint(47000, 47999)),
			'X-ZERO-F-DEVICE-ID': dev_id,
			'X-ZERO-STATE': 'unknown',
			'app-scope-id-header': str(uuid.uuid4()),
			'x-zero-eh': '664c0faaac849cb891d0a261fbb72a12',
			'x-tigon-is-retry': 'False',
			'x-fb-client-ip': 'True',
			'x-fb-server-cluster': 'True',
		}

		payload = {
			'adid': str(uuid.uuid4()),
			'format': 'json',
			'device_id': str(uuid.uuid4()),
			'email': user,
			'password': password,
			'generate_analytics_claim': '1',
			'community_id': '',
			'cpl': 'true',
			'family_device_id': dev_id,
			'secure_family_device_id': str(uuid.uuid4()),
			'credentials_type': 'password',
			'generate_session_cookies': '1',
			'generate_machine_id': '1',
			'meta_inf_fbmeta': 'NO_FILE',
			'advertiser_id': str(uuid.uuid4()),
			'currently_logged_in_userid': '0',
			'locale': 'id_ID',
			'client_country_code': 'ID',
			'method': 'auth.login',
			'fb_api_req_friendly_name': 'authenticate',
			'fb_api_caller_class': 'com.facebook.account.login.protocol.LegacyAuthenticator',
			'api_key': self.api_key,
			'access_token': self.token,
		}
		try:
			response = requests.post("https://b-graph.facebook.com/auth/login", data=payload, headers=headers)
			print(response.text)
			return response
		except Exception as e:
			print(f"[!] Error: {str(e)}")
			return None

if __name__ == "__main__":
	email_akun = "" # ISI EMAIL FACEBOOK KAMU
	pass_akun = "" # ISI PASSWORD FACEBOOK KAMU
	bot = MetaBusiness()
	res = bot.login_request(email_akun, pass_akun)
