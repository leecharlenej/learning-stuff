# Introduction
These are my notes for following YouTube - Software Engineering Skills: Creating an Angular Portfolio.

Note that the versions I am using are:
- Angular CLI: 18.1.3
- Node: 20.16.0
- Boostrap: ^5.2.3
---

## Setting up environment
1. To check version of Angular: `ng version`
- **Error:** `\npm\ng.ps1 cannot be loaded because running scripts is disabled on this system.`
- **Solution:** Go to `C:\Users\{user_name}\AppData\Roaming\npm`. Delete `ng.ps1`


2. To create a new project: Go to folder > `ng new`
- The above will create the latest version of Angular, which does not have `app.module.ts`.
- To create a new project with modules: `ng new my-app --no-standalone --routing --ssr=false`
- For single-page application: `Do you want to enable Server-Side Rendering (SSR) and Static Site Generation (SSG/Prerendering)?` No.

3. To build project: Right-click on project. > Select `Open in Integrated Terminal`. > `ng serve`
- **Error:** `This command is not available when running the Angular CLI outside a workspace.`
- **Solution:** Make sure you 'open in integrated terminal'.

## Installed files

1. `src/index.html`: Contains whole website.
- `<app-root></app-root>`: Entry point for Angular app. Points to `app.component.ts`: `selector: 'app-root'`

2. `src/app/app.component.html`: Contains CSS and HTML code that are displayed on website.

3. Angular components: Build different sections of the website and are made of 3 parts.
- `src/app/app/app.component.html`: HTML template
- `src/app/app/app.component.css`: Associate style sheet for the component. vs `styles.css`: Defined globally
- `src/app/app/app.component.ts`: Add functionality to component.

4. `src/app/app.module.ts`: Modules imported for added functionality.
- `selector`: Use to identify different components.

5. `\angular.json`: Tells project where to find files and set configurations.

## Coding tips
1. `{{}}`: Insert data from a variable in a component file into HTML.

2. `<webElement>.<class>`: Create an element with the class.

## Bootstrap
1. To install bootstrap: `ng add ngx-bootstrap`
- An open-source CSS framework that contains CSS and JS classes to make website responsive.

## Components
1. To create a new component: `ng g c header --skip-tests` or `ng generate component`
- By default, a test file will be generated as well. Skip this if it is a static file.

2.  Add to app.component.html: `<componentName></componentName>`
