# DorkKnight - Google Dorking and Vulnerability Discovery Tool

"DorkKnight" is a powerful and versatile Python script designed to empower ethical hackers, cybersecurity researchers, and penetration testers in their quest to uncover potential vulnerabilities and exposed information on the internet. Leveraging advanced search techniques known as "Google dorking," this tool enables you to perform targeted searches on specific domains, revealing hidden or sensitive data that could pose a security risk.

## Features

- Perform targeted "Google dorking" queries on a specified target domain to discover potential security vulnerabilities, exposed credentials, and sensitive information.
- Utilize the Google Custom Search JSON API to retrieve search results efficiently.
- Clearly present discovered links along with insightful explanations for a comprehensive understanding of the findings.
- Designed to assist in ethical hacking, vulnerability assessment, and security research.

## Prerequisites

- Python 3.x
- `requests` library (install with `pip install requests`)
- Google API key and Custom Search Engine ID (instructions included below)

## Getting Started

1. **Obtain Google API Key and Custom Search Engine ID:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or use an existing one.
   - Enable the "Custom Search JSON API" for your project.
   - Create credentials and select "API Key."
   - Copy the generated API key.
   
2. **Create Custom Search Engine:**
   - Go to [Google Custom Search](https://programmablesearchengine.google.com/about/).
   - Click on "Create a Programmable Search Engine."
   - Follow the setup process to create a new search engine.
   - In "Sites to Search," add the sites you want to search.
   - Once the search engine is created, go to "Control Panel" > "Details" and copy the "Search Engine ID."

## How to Use

1. Run the script from the command line:
   ```bash
   python DorkKnight.py target_domain api_key cx
   
- Replace the placeholders for `target`, `api_key`, and `cx` with your actual Google API key and Custom Search Engine ID.

## Contributing

"DorkKnight" is an open-source project, and we welcome contributions from the community to enhance its capabilities and extend the list of useful dork queries. If you have valuable dork queries to add, we encourage you to submit a pull request with your additions.

### Adding New Dork Queries

To add new dork queries to "DorkKnight," follow these steps:

1. **Fork the Repository:** Start by forking the repository to your GitHub account.
2. **Edit the Dork Queries:** Open the `DorkKnight.py` file in a text editor.
3. **Locate the Dork Queries:** Find the `dork_queries` list within the `dorkisation` function.
4. **Add New Queries:** Add your new dork query using the format: `(f"site:{mytarget} your_dork_query_here", "Description of your query.")`.
5. **Save and Commit:** Save the file and commit your changes to your forked repository.
6. **Create a Pull Request:** Open a pull request to the original repository, explaining the new dork queries you've added and their purpose.

Please ensure that any new dork queries you contribute are relevant to the tool's ethical and security-focused usage. Your contributions will help make "DorkKnight" even more valuable to the cybersecurity community.

### Suggestions and Improvements

If you have suggestions for improving the tool, enhancing its functionality, or addressing any issues, feel free to open an issue on GitHub. We appreciate your feedback and are dedicated to making "DorkKnight" the best tool it can be.

Thank you for contributing to the security community by helping us build a more comprehensive and effective dorking tool!

