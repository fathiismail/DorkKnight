import requests
import argparse

def perform_google_search(query, api_key, cx, num_results=10):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx,
        "num": num_results
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if "items" in data:
            search_results = [item["link"] for item in data["items"]]
            return search_results
        else:
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def apply_dork_query(dork_query, explanation, api_key, cx):
    search_results = perform_google_search(dork_query, api_key, cx, num_results=10)

    if search_results:
        print("Dork Query:")
        print(dork_query)
        print("Explanation:")
        print(explanation)
        print("Links Discovered:")
        for link in search_results:
            print(link)
    else:
        print("No links discovered.\n")

def dorkisation(mytarget, api_key, cx):
    # List of dork queries and explanations
    dork_queries = [
    (f"site:{mytarget} allintext: username filetype: log ", "This dork searches for log files containing the word 'username'. It is useful for finding log files that may contain sensitive information."),
    (f"site:{mytarget} inurl: / proc / self / cwd", "This dork is used to detect vulnerable or hacked servers that allow you to add '/proc/self/cwd/' directly to the website URL"),
    (f"site:{mytarget} 'index of' inurl: ftp", "This dork is used to explore public FTP servers that may reveal interesting information."),
    (f"site:{mytarget} .env intext: username password", " This dork searches for .env files that may contain unencrypted usernames and passwords."),
    (f"site:{mytarget} intitle: index.of id_rsa -id_rsa.pub", "This dork is used to find SSH private keys indexed by Google."),
    (f"site:{mytarget} filetype: xls inurl: 'email.xls' ", "This dork searches for Excel files that may contain email addresses."),
    (f"site:{mytarget} inurl: top.htm inurl: currenttime", "This dork is used to find live camera web pages that are not IP restricted."),
    (f"site:{mytarget} intitle: index of mp3", "This dork searches for directories containing MP3 files."),
    (f"site:{mytarget} inurl: zoom.us/j and intext: scheduled", "This dork is used to find Zoom meeting URLs."),
    (f"site:{mytarget} 'Index of'' 'database.sql.zip' ", "This dork searches for compressed SQL dump files."),
    (f"site:{mytarget} intitle: 'Index of' wp-admin", "This dork searches for WordPress admin login pages."),
    (f"site:{mytarget} intitle: 'Apache2 Ubuntu Default Page: It works'", "This dork searches for Apache2 web pages."),
    (f"site:{mytarget} inurl: Dashboard.jspa intext: 'Atlassian Jira Project Management Software'", "This dork searches for JIRA instances."),
    (f"site:{mytarget} inurl: _cpanel / forgotpwd", "This dork searches for cPanel password reset pages."),
    (f"site:{mytarget} allintitle: restricted filetype: doc site: gov", "This dork searches for restricted government documents."),
    (f"site:{mytarget} -www -shop -share -ir -mfa", "Exclude certain terms to filter out unwanted results and potentially reveal hidden or vulnerable information."),
    (f"site:pastebin.com '{mytarget}' ", "Search for code snippets on Pastebin where sensitive information might have been accidentally exposed."),
    (f"site:jsfiddle.net '{mytarget}' ", "Search for code snippets on JSFiddle, which developers might have shared publicly, potentially containing vulnerabilities."),
    (f"site:codebeautify.org '{mytarget}' ", "Search for code on Codebeautify, where developers may have shared code snippets.."),
    (f"site:codepen.io '{mytarget}' ", "Search for code snippets on CodePen related to the specified domain, which could expose sensitive code."),
    (f"site:{mytarget} ext:php inurl:? ", "Search for PHP files on the specified domain with query parameters, revealing potential vulnerabilities."),
    (f"site:openbugbounty.org inurl:reports intext:'{mytarget}' ", "Search for disclosed bug bounties related to Yahoo.com on OpenBugBounty."),
    (f"site:docs.google.com inurl:'/d/'' '{mytarget}' ", "Search Google Docs URLs for sensitive data related to the specified domain."),
    (f"site:onedrive.live.com '{mytarget}' ", "Search OneDrive URLs for accidentally public files and photos related to the specified domain."),
    (f"site:dropbox.com/s '{mytarget}' ", "Search Dropbox URLs for links to sensitive content related to the specified domain."),
    (f"site:box.com/sm '{mytarget}' ", " Search Box URLs for sensitive files related to the specified domain."),
    (f"site:dev.azure.com '{mytarget}' ", "Search Azure DevOps URLs for critical information like API keys and unsecured repositories related to the specified domain."),
    (f"site:http://sharepoint.com '{mytarget}' ", "Search SharePoint URLs for publicly accessible internal communications and records related to the specified domain."),
    (f"site:{mytarget} filename:vim_settings.xml", "information disclosure"),
    (f"site:{mytarget} filename:secrets.yml", "information disclosure"),
    (f"site:{mytarget} filename:config.json", "information disclosure"),
    (f"site:{mytarget} filename:config.ini", "information disclosure"),
    (f"site:{mytarget} filename:http://config.properties", "information disclosure"),
    (f"site:{mytarget} filename:config.xml", "information disclosure"),
    (f"site:{mytarget} filename:config.yml", "information disclosure"),
    (f"site:{mytarget} filename:credentials.json", "information disclosure"),
    (f"site:{mytarget} filename:credentials.xml", "information disclosure"),
    (f"site:{mytarget} inurl:config pass", "This dork searches for 'config' URLs that contain 'pass'."),
    (f"site:{mytarget} inurl:config secret", "This dork searches for 'config' URLs that contain 'secret'."),
    (f"site:{mytarget} inurl:config.php dbpasswd", "This dork searches for 'config.php' URLs that contain 'dbpasswd'."),
    (f"site:{mytarget} inurl:config.php pass", "This dork searches for 'config.php' URLs that contain 'pass'."),
    (f"site:{mytarget} inurl:config.php password", "This dork searches for 'config.php' URLs that contain 'password'."),
    (f"site:{mytarget} inurl:configuration", "This dork searches for 'configuration' URLs."),
    (f"site:{mytarget} inurl:env", "This dork searches for 'env' URLs."),
    (f"site:{mytarget} inurl:setting", "This dork searches for 'setting' URLs."),
    (f"site:{mytarget} filetype:log", "This dork searches for log files."),
    (f"site:{mytarget} intext:\"Index of /\" +.htaccess", "This dork searches for .htaccess files in directories."),
    (f"site:{mytarget} intitle:\"index of\"", "This dork searches for directory listings."),
    (f"site:{mytarget} inurl:& intext:admin intext:login", "This dork searches for admin login URLs."),
    (f"site:{mytarget} inurl:& intext:search", "This dork searches for URLs with 'search' in them."),
    (f"site:{mytarget} inurl:config secret", "This dork searches for 'config' URLs that contain 'secret'."),
    (f"site:{mytarget} inurl:backup", "This dork searches for 'backup' URLs."),
    (f"site:{mytarget} inurl:backup.zip", "This dork searches for 'backup.zip' URLs."),
    (f"site:{mytarget} inurl:quiz inurl:&", "This dork searches for 'quiz' URLs with query parameters."),
    (f"site:{mytarget} inurl:Makefile.toml", "This dork searches for 'Makefile.toml' URLs.")

    ]

    # Apply dork queries to the target and display results
    for dork_query, explanation in dork_queries:
        try:
            apply_dork_query(dork_query, explanation, api_key, cx)
        except Exception as e:
            print("An error occurred:", str(e))
        print("=" * 50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform Google Dorking on a target domain.")
    parser.add_argument("target", help="Target domain to perform dorking on.")
    parser.add_argument("api_key", help="Google API key.")
    parser.add_argument("cx", help="Custom Search Engine ID.")
    args = parser.parse_args()

    dorkisation(args.target, args.api_key, args.cx)
