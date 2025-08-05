---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - documentation
  - python
---
[PDOC](https://pdoc.dev/) is a documentation generator specifically designed for Python projects:

1. **Automatic Documentation**: It scans your Python code and automatically generates documentation based on the docstrings you include in your code. This means that as long as you write clear comments and descriptions in your code, pdoc can create documentation without much extra work.

2. **Modern and Clean Design**: The output documentation is visually appealing and easy to navigate. It uses a modern design that enhances readability, making it user-friendly for anyone who needs to understand your code.

3. **Customization Options**: While pdoc generates documentation automatically, it also allows for some customization. You can configure settings to adjust how the documentation looks and what content is included.

4. **Markdown Support**: pdoc supports Markdown, which means you can use Markdown syntax in your docstrings to format your documentation with headings, lists, links, and more.

5. **Easy Integration**: It can be easily integrated into your development workflow, allowing you to generate documentation as part of your build process or whenever you need it.

6. **No Manual Guides Required**: With pdoc, you can avoid the tedious task of writing extensive documentation manually. Instead, you can focus on writing code, and pdoc will handle the documentation generation for you.

Once you generate the HTML files using [[pdoc]], you have several options for what to do with them:

1. **Local Viewing**: You can open the generated HTML files directly in your web browser to view the documentation locally. This is useful for personal reference or for sharing with a small team.

2. **Hosting on a Web Server**: You can upload the generated HTML files to a web server to make the documentation accessible to a wider audience. This is a common practice for open-source projects or any project where you want to share documentation with users or collaborators.

3. **Integrating with Project Repositories**: If you're using version control systems like Git, you can include the generated documentation in your repository. This way, anyone who clones the repository can access the documentation easily.

4. **Publishing to Documentation Platforms**: You can publish the HTML files to documentation hosting platforms like Read the Docs, GitHub Pages, or similar services. These platforms often provide additional features like versioning, search functionality, and easy navigation.

5. **Archiving**: You can keep the generated HTML files as part of your project archive for future reference. This is useful for maintaining a history of your documentation as your project evolves.

6. **Sharing with Stakeholders**: If you are working on a project with stakeholders or clients, you can share the HTML documentation with them to provide insights into the project's structure and functionality.

To explicitly tell pdoc to document the local `scripts` directory, you need to prepend `./` to the directory name.

Here’s how to do it:

1. **Open your terminal**.
2. **Navigate to the directory** where your `scripts` folder is located (which seems to be `C:\Users\RhysL\Desktop\Auto_YAML`).
3. **Run the pdoc command** with the `-o` option and prepend `./` to the `scripts` directory name:

   ```bash
   pdoc -o docs ./scripts
   ```

This command tells pdoc to generate documentation for the local `scripts` directory and save the output in the `docs` folder.

After running this command, you should find the generated documentation in the `docs` folder, which you can then open in your web browser.

## what to do next

1. **View Locally**: Open the HTML files in your web browser to view the documentation. You can start by opening the `index.html` file in the `docs` folder. This file typically serves as the main entry point for your documentation

2. **Host on a Web Server**: If you want to make the documentation accessible online, you can upload the `docs` folder to a web server. This could be a personal website, a cloud storage service that supports HTML hosting, or a documentation hosting platform like GitHub Pages or Read the Docs.
    
3. **Integrate into a Project Repository**: If you're using version control (like Git), you can include the `docs` folder in your repository. This way, anyone who clones the repository can easily access the documentation.