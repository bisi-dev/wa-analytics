# wa-analytics
A Python Data Analytics Flask application that provides Insights from WhatsApp chats

# WA - Analytics

#### A web app for analysing WhatsApp Group Chats.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-green)](https://opensource.org/licenses/Apache-2.0) 

WA-Analytics is a web app built with Python/Flask that enables users to analyse and source insights from WhatsApp chats.

<a href="https://wa-analytics.herokuapp.com/" target="_blank"><strong>>> LIVE WEB APP</strong></a>

· <a href="#how-to-start">How to Start</a>· <a href="#feedback">Feedback</a>· <a href="#license">License</a>



---

## How to Start

Pre-Requisites: Python 3.0+

After Forking/Cloning, you can get up and running in just a few minutes. From the project's root folder:

1. **Install all required packages.**

   ```
   pip install requirements.txt
   ```

2. **Start your local flask server.**

   ```
   python main.py
   ```

3. **Voila! View app in any browser at http://127.0.0.1:5000/**

---
## Feedback

I always appreciate feedback, so share your thoughts and suggestions with me: [mail@bisi.dev](mailto:yinka.olabisi@yahoo.com)

If you find any bugs or have feature suggestions, create a new issue or pull request 🙏

Thanks a lot! 💪

Ayodeji Olabisi – [bisi.dev](https://bisi.dev)

---

## License

Distributed under the [Apache-2.0](https://opensource.org/licenses/Apache-2.0) license.

See `LICENSE` for more information.

<!--
<a href="#sections">Sections</a> · <a href="#features">Features</a> · <a href="#how-to-start">How to Start</a> · <a href="#edit-content">Edit Content</a> · <a href="#edit-theme">Edit Theme</a> · <a href="#edit-page-structure">Edit Page Structure</a> · <a href="#feedback">Feedback</a>
**New Features:** 🌛 Dark Mode · 🪟 Splash Screen · 🍪 Cookie Consent Bar
<img src="screenshot.png" alt="Image" width="600" />
## Sections

The starter has predefined sections as well as a template that you can use to create new, custom sections.

**The predefined sections are:**

1. About me
2. Interests/Skills
3. Projects
4. Contact me
5. Medium articles

---

## Features

#### 🍪 [NEW] Cookie Consent Bar - Be ready for GDPR-compliant tracking.

Add tracking services like Google Analytics to your site and display a GDPR-compliant cookie consent banner.

#### 🌛 [NEW] Dark Mode - Based on user's preferences.

If the user's OS is set to using dark mode, the Gatsby Starter will automatically switch to a dark theme too.

#### 🕹️ Quick and Easy Setup - Add content and deloy.

Just install the starter, add your content, and deploy it! This starter works seamlessly with hosts like Netlify.

#### 📓 Content Integration via MDX - No external CMS needed.

MDX is a Markdown format that allows you to enrich your content with React components. This makes it fully customizable without external dependencies.

#### 🧰 Extendable Layout - Add more sections as you like.

The starter includes predefined sections as well as a template for new, custom sections. Moreover, you can add new projects to the project section without additional coding.

#### 💅 Responsive Design - With freshening animations.

The starter is designed with a mobile-first approach and looks perfect on small and large breakpoints. Moreover, it has some nice and smooth animations.

#### <img src="http://logok.org/wp-content/uploads/2015/10/Medium-logo-old.png" alt="Medium Icon" width="20" /> Medium Integration - Features latest articles.

In case you are a writer on Medium, the starter has a easy to use Medium integration that allows you to feature your latest articles.

To see all features in action, have a look at the <a href="https://gatsby-starter-portfolio-minimal.netlify.app/" target="_blank"><strong>live demo</strong></a>.

## Edit Content

After you installed the starter project, you most likely want to add your own content.

### Edit configuration

First, you want to edit the config file which stores the site's configuration (e.g. title, description) and social profiles.

```
|-- config
    |-- index.js
```

Navigate to the `index.js` file in the config folder, edit the configuration, save it, that's it!

### Edit page content

Next, you can edit the content for each section you want to be displayed. By default, all sections are shown. If you want to remove certain sections from the site, check out <a href="#editing-page-structure">this part of the Readme</a>.

```
|-- content
    |-- imprint
    |-- index
       |-- about
       |-- contact
       ...
    ...
```

You find all content in the content folder (surprisingly). For content integration, the project uses MDX, a Markdown format. If you haven't worked with Markdown or MDX before, check the Markdown syntax in <a href="https://www.gatsbyjs.org/docs/mdx/markdown-syntax/" target="_blank">Gatsby's docs</a>. They also provide <a href="https://www.gatsbyjs.org/docs/mdx/writing-pages/" target="_blank">further information about MDX</a>.

To get up and running, just edit the predefined data fields in each `mdx` file.

---

## Edit Theme

You find the color and font settings in the configuration file, located at: `config/index.js`.

> Note: The usage of the splash screen can be set for each page individually in the page content directory.

---

## Edit Page Structure

To remove or reorder predefined sections, navigate to the `src/pages/index.js` file. This is the home page of your site.

Each section (besides the Articles section) exists of an imported React component and a GraphQL query that is needed for data querying.

**If you want to remove a section**, just delete the imported React component and query.

**If you want to reorder your sections**, just reorder the React components inside the `<Layout />` component.

### Add custom sections

If you want to add your own custom sections, there is a section template you can use. You can find it in the following directory: `src/components/templates`

---



Truffle is a development environment, testing framework and asset pipeline for Ethereum, aiming to make life as an Ethereum developer easier. With Truffle, you get:

* Built-in smart contract compilation, linking, deployment and binary management.
* Automated contract testing with Mocha and Chai.
* Configurable build pipeline with support for custom build processes.
* Scriptable deployment & migrations framework.
* Network management for deploying to many public & private networks.
* Interactive console for direct contract communication.
* Instant rebuilding of assets during development.
* External script runner that executes scripts within a Truffle environment.

| ℹ️ **Contributors**: Please see the [Development](#development) section of this README. |
| --- |

### Install

```
$ npm install -g truffle
```

*Note: To avoid any strange permissions errors, we recommend using [nvm](https://github.com/nvm-sh/nvm).*

### Quick Usage

For a default set of contracts and tests, run the following within an empty project directory:

```
$ truffle init
```

From there, you can run `truffle compile`, `truffle migrate` and `truffle test` to compile your contracts, deploy those contracts to the network, and run their associated unit tests.

Truffle comes bundled with a local development blockchain server that launches automatically when you invoke the commands  above. If you'd like to [configure a more advanced development environment](https://trufflesuite.com/docs/advanced/configuration) we recommend you install the blockchain server separately by running `npm install -g ganache-cli` at the command line.

+  [ganache](https://github.com/trufflesuite/ganache): a command-line version of Truffle's blockchain server.
+  [ganache-ui](https://github.com/trufflesuite/ganache-ui): A GUI for the server that displays your transaction history and chain state.


### Documentation

Please see the [Official Truffle Documentation](https://trufflesuite.com/docs/) for guides, tips, and examples.

### Development

We welcome pull requests. To get started, just fork this repo, clone it locally, and run:

```shell
# Install
npm install -g yarn
yarn bootstrap

# Test
yarn test

# Adding dependencies to a package
cd packages/<truffle-package>
yarn add <npm-package> [--dev] # Use yarn
```

If you'd like to update a dependency to the same version across all packages, you might find [this utility](https://www.npmjs.com/package/lerna-update-wizard) helpful.

*Notes on project branches:*
+    `master`: Stable, released version (v5)
+    `beta`: Released beta version
+    `develop`: Work targeting stable release (v5)
+    `next`: Not currently in use

Please make pull requests against `develop`.

There is a bit more information in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

### License

MIT
-->
