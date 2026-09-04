import os
import tempfile
import unittest

from scanner import analyze_url, save_scan


class TestURLScanner(unittest.TestCase):
    def test_https_clean_url(self):
        result = analyze_url("https://google.com")
        self.assertEqual(result["risk"], "0/9")
        self.assertEqual(result["result"], "LOW RISK")
        self.assertEqual(result["warnings"], [])

    def test_http_ip_login_url(self):
        result = analyze_url("http://192.168.1.25/login")
        self.assertEqual(result["risk"], "3/9")
        self.assertEqual(result["result"], "MEDIUM RISK")
        self.assertIn("No HTTPS", result["warnings"])
        self.assertIn("IP address used", result["warnings"])
        self.assertIn("Suspicious words: login", result["warnings"])

    def test_history_is_saved(self):
        with tempfile.TemporaryDirectory() as folder:
            history_file = os.path.join(folder, "history.json")
            record = analyze_url("https://example.com")
            saved = save_scan(record, history_file)

            self.assertTrue(os.path.exists(history_file))
            self.assertEqual(saved["url"], "https://example.com")
            self.assertIn("time", saved)


if __name__ == "__main__":
    unittest.main()
