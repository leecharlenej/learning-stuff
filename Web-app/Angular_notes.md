# Introduction
These are my notes for following YouTube - Software Engineering Skills: Creating an Angular Portfolio.

Note that the versions I am using are:
- Angular CLI: 18.1.3
- Node: 20.16.0
- Boostrap: ^5.2.3
---
## Contents
1. [Setting up environment](#settingupenv)
2. [Angular installed files](#explaininstalledfiles)
3. [Bootstrap](#bootstrap)
4. [Angular components](#angularcomponents)
5. [Angular variable components](#angularvarcomponents)
6. [Coding Tips](#codingtips)
7. [Troubleshoot](#troubleshoot)
---
<a id="settingupenv"></a>
## Setting up environment

| Action   | Command |
| -------- | ------- |
| 1. To check version of Angular             | `ng version`   |
| 2. To create new project w/o modules       | Go to folder. > `ng new`    |
| 3. To create new project w _app.module.ts_ | `ng new my-app --no-standalone --routing --ssr=false`   |
| 4. To build project                        | `ng serve`   |

- For single-page application: _Do you want to enable Server-Side Rendering (SSR) and Static Site Generation (SSG/Prerendering)?_ No.

<a id="explaininstalledfiles"></a>
## Angular installed files

| File name   | Purpose |
| ----------- | ------- |
| _src/index.html_             | Contains whole website.  |
| _src/app/app.component.html_ | Contains CSS and HTML code that are displayed on website. |
| Angular components - _src/app/app/app.component.html, app.component.css, app.component.ts_ | HTML template, associated style sheet, adds funtionality to component. |
| _src/app/app.module.ts_  | Modules imported for added functionality.|
| _angular.json_ | Tells project where to find files and to set configurations.|

- `<app-root></app-root>`: Entry point for Angular app. Points to _app.component.ts_: _selector_: _app-root_
- _styles.css_: Defined globally
- _selector_: Use to identify different components.

<a id="bootstrap"></a>
## Bootstrap
- An open-source CSS framework that contains CSS and JS classes to make website responsive.
- To install bootstrap: `ng add ngx-bootstrap`

<a id="angularcomponents"></a>
## Angular Components

| Action   | Command |
| -------- | ------- |
| To create new component | `ng g c header --skip-tests` or `ng generate component` |
| To add components to main website | Go to _app.component.html_. > `<componentName></componentName>` |
| To link to components/ add routing to website | Go to _app.component.html_. > `router-outlet></router-outlet>` |
| To configure routing to different components | Go to _app-routing.module.ts_. > Import component and add to _Routes_ list.
| To check if component is working | Go to `/<componentName` in browser. |

- When creating new component, by default, a test file will be generated as well. Skip this if it is a static file.

<a id="angularvarcomponents"></a>
## Angular variable Components
The same component template can be used repeatedly, as in the case of the _project-card_. 

### Method 1
1. Add `<app-project-card></app-project-card>` to _portfolio.component.html_.
2. Go to _project-card-component.html_ to edit HTML.
3. To supply different data to the component, use parent-child communication. In this case, parent = _portfolio.component.html_ and child = _app-project-card_ component. Go to _project-card-components.ts_ and use _@Input decorator_. Go to _project-card-component.html_ and use _{{}}_ for variable data with single quotes.

### Method 2: Use Typescript class modal to hold data.
1. Go to folder _app_, create folder __modals_ and file _project.ts_.
2. Go to file _project.ts_, add interface and accompanying properties (Strings, arrays etc.) for the variable data.
3. Go to _project-card.components.ts_, add the interface.
4. Go to _project-card.component.html_, add in all variable data names.
- For arrays, use _ngFor_.

<a id="codingtips"></a>
## Coding tips
1. `{{}}`: To insert data from a variable in component file into HTML.

2. `<webElement>.<class>`: To create an element with the specified class.

<a id="troubleshoot"></a>
## Troubleshoot
1. **Error:** `\npm\ng.ps1 cannot be loaded because running scripts is disabled on this system.`
- **Solution:** Go to `C:\Users\{user_name}\AppData\Roaming\npm`. Delete `ng.ps1`

2. **Error:** `This command is not available when running the Angular CLI outside a workspace.`
- **Solution:** Make sure you 'open in integrated terminal'.

3. **Missing:** assets folder has been replaced with public folder in latest Angular version.
- **Solution:** To refer to an image, use `<img src="<imageName>.jpeg">`


