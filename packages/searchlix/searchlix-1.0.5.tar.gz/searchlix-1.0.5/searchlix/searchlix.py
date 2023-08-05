import requests
import re
from bs4 import BeautifulSoup
import dns.resolver

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)


def find_phone_number(text):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

def find_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails


def extract_email_from_link(url):
    response = requests.get(url, allow_redirects=False, verify=False, timeout=15)
    html_content = response.text
    # Search for email addresses using regular expressions
    emails = find_email(html_content)
    if emails:
        # Print the email addresses found
        for email in emails:
            print(email)
        return emails
    else:
        print("Could not found any emails")


def extract_phone_from_link(url):
    response = requests.get(url, allow_redirects=False, verify=False, timeout=15)
    html_content = response.text

    phone_numbers = find_phone_number(html_content)
    if phone_numbers:
        for phone_number in phone_numbers:
            print(phone_number)
        return phone_numbers
    else:
        print("Could not found any phone numbers")


def pattern_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # Construct prefix table
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j-1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j

    # Search for pattern in text
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j-1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                return i - m + 1

    return 0


def extract_page_url(url, page_name):
    response = requests.get(url, allow_redirects=False, verify=False, timeout=15)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links in the HTML content
    links = []
    url_found = {}
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

    # Print the links
    for link in links:
        result = pattern_search(link, page_name)
        if result:
            if link in url_found:
                url_found[link] += 1
            else:
                url_found[link] = 1
    return url_found


def check_mail_server(domain):
    domain = re.sub(r'(www\.|http(s)*://)', '', domain)
    try:
        result = dns.resolver.resolve(domain, 'MX')
        for exdata in result:
            if exdata:
                return True
            return False
    except dns.resolver.NXDOMAIN:
        return False
    except dns.resolver.Timeout:
        return "Timed out while resolving"


def is_valid_domian(domain):
    domain = re.sub(r'(www\.|http(s)*://)', '', domain)
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ip in result:
            if ip:
                return True
            return False
    except dns.resolver.NXDOMAIN:
        return False
    except dns.resolver.Timeout:
        return "Timed out while resolving"
    

t = check_mail_server('https://www.domains.tm')
print(t)