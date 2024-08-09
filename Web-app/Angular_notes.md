# Introduction
These are my notes for following [Software Engineering Skills: Creating an Angular Portfolio.](https://www.youtube.com/playlist?list=PLN0Th-4WgKrUVQlqa14mUDeymTW1luznW)

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
6. [Setting up service](#settingupservice)
7. [Adding modal](#addmodal)
8. [Adding carousel](#addcarousel)
9. [Adding filter](#addfilter)
10. [Deploying onto Github pages](#deploygithub)
10. [Coding Tips](#codingtips)
11. [Troubleshoot](#troubleshoot)
12. [Reflections](#reflections)
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
| To link to components add routing to website | Go to _app.component.html_. > `<router-outlet></router-outlet>` |
| To configure routing to different components | Go to _app-routing.module.ts_. > Import component and add to _Routes_ list.
| To check if component is working | Go to `/<componentName` in browser. |

- When creating new component, by default, a test file will be generated as well. Skip this if it is a static file.

<a id="angularvarcomponents"></a>
## Angular variable Components
The same component template can be used repeatedly, as in the case of the _project-card_. 

### Method 1
1. Add `<app-project-card></app-project-card>` to _portfolio.component.html_.
2. Go to _project-card-component.html_ to edit HTML.
3. To supply data to the component, use parent-child communication. In this case, parent = _portfolio.component.html_ and child = _app-project-card_ component. Go to _project-card-components.ts_ and use _@Input decorator_. Go to _project-card-component.html_ and use _{{}}_ for variable data with single quotes.

### Method 2: Use Typescript class modal to hold variable data.
1. Go to folder _app_, create folder __modals_ and file _project.ts_.
2. Go to file _project.ts_, add interface and accompanying properties (Strings, arrays etc.) for the variable data.
3. Go to _project-card.components.ts_, add the interface.
4. Go to _project-card.component.html_, replace hard-coded values with variable data names.
- For arrays, use _ngFor_. Remember to use _{{}}_.
5. Go to _portfolio.component.ts_ and add a project with its details.
6. Go to _porfolio.component.html_ and add this project. Project cards now display the data supplied by portfolio component.
7. For arrays, enum can only be defined by primitive data types like strings. Tags come with colours, hence create a modal for it. Remember to add Tag modal to _project.ts_, _portfolio.component.ts_ and _project-card.component.html_ (Angular data binding: Overwrites default value with data it is bounded to dynamically. ).

<a id="settingupservice"></a>
## Setting up Service
Service provides the same set of functionality to any components. It is usually used to fetch data from API endpoints and then, supplied to components. In this case, Variable data (projects) only exist in porfolio component and cannot be accessed by other components. Hence, the need to set up a service.

1. To create a service, go to folder _services_, open up a terminal and `ng g s projects --skip-tests`.
- Different from a component; no associated HTML and CSS files. Class is an injectable.
2. Go to _projects.service.ts_ to create database of projects and the accompanying methods.
3. To use service, go to component, add in to constructor and implement _Oninit_ interface.
4. Edit the HTML file.

<a id="addmodal"></a>
## Adding modal
Modal is a pop-up window that overlays on the side.
1. Go to _app.module.ts_ and add the modal.
2. Go to _project-card.component.ts_ to add the modal.
3. Go to _project-card.component.html_ to add it as a click event.
4. Create a project-modal component to hold the HTML for the modal. `ng g c project-modal --skip-tests`
5. Go to _project-modal.component.ts_ to add BsModalRef.
6. Go to _project-card.component.ts_ to add project modal component.

<a id="addcarousel"></a>
## Adding Carousel
1. Go to _app.module.ts_ and add the carousel.

<a id="addfilter"></a>
## Adding filters
(_To be filled in._)

<a id="deploygithub"></a>
## Deploying onto Github pages
There are many ways to do this but for now, this works the best for me (with the least number of errors encountered.).

Reference website: [(here)](https://www.linkedin.com/pulse/deploy-angular-app-github-pages-cli-dilakshan-antony-thevathas-octlc/)

1. `ng build` to create the folder `dist`.
2. Copy the contents in this folder into a new folder.
3. Create a new repository for it.
4. In _index.html_, change to `<base href="/<REPONAME>/">` and push all changes to the repo.
5. Go to _Github_ > _Settings_ > _Pages_ > Under _Branch_, change to _main/root_ and save.
6. Go to _Actions_ tab to check the deployment and you are done! \(:

<a id="codingtips"></a>
## Coding tips
1. `{{}}`: To insert data from a variable in component file into HTML.

2. `<webElement>.<class>`: To create an element with the specified class.

<a id="troubleshoot"></a>
## Troubleshoot
### During installation.

1. **Error:** _\npm\ng.ps1 cannot be loaded because running scripts is disabled on this system._
- **Solution:** Go to `C:\Users\{user_name}\AppData\Roaming\npm`. Delete `ng.ps1`

2. **Error:** _This command is not available when running the Angular CLI outside a workspace._
- **Solution:** Make sure you 'open in integrated terminal'.

3. **Missing:** assets folder has been replaced with public folder in latest Angular version.
- **Solution:** To refer to an image, use `<img src="<imageName>.jpeg">`

4. **Error:** _Error: Cannot resolve type entity i4.FocusTrapModule to symbol_
- **Solution:** Go to _tsconfig.json_, change to `"compilerOptions": { ... "moduleResolution": "node", ... }`.

5. **Error:** Page isn't loading properly.
- **Solution:** `ng cache clean`

During deployment on Github Pages.
1. **Error:** _▲ [WARNING] bundle initial exceeded maximum budget. Budget 512.00 kB was not met by 208.10 kB with a total of 720.10 kB._
- **Solution:** Go to _angular.json_, change `"budgets": [ ... "maximumWarning": 500kB, ...]`

2. **Error:** _[WARNING] 2 rules skipped due to selector errors: .form-floating>~label -> Did not expect successive traversals._
- **Solution:** Go to _angular.json_, add the following under `"configurations": {"production": {`, just before `"budgets":`. (Reference: [(here)](https://github.com/ng-bootstrap/ng-bootstrap/issues/4306))

```
"optimization": {
              "scripts": true,
              "styles": {
                "minify": true,
                "inlineCritical": false
              }},
  ````

3. **Error:** (When using `ng deploy` method.) _The git repository has too many active changes, only a subset of Git features will be enabled. Would you like to add "node_modules" to .gitignore?_
- **Solution:** _(Not found yet.)_

4. **Error:** Images are not showing on Github Page.
- **Solution:** Remove _/_ at the start of the image URLs.

5. **Error:** Github page displays 404 error after a while.
- **Solution:** Copy and paste _index.html_ in same repo folder and rename it as _404.html_.


---
<a id="reflections"></a>
## Reflections
I use YouTube extensively to understand my school materials and to develop automation scripts. However, this is the first time that I have used it to embark on such a massive project. And it has been challenging. Programmes are always being updated and so, one can't always follow to the tee. You need to find the equivalent in the new version but this is okay because usually these are documented. It is when you encounter errors and the troubleshooting process seems never-ending that it can get frustrating. (And sometimes, there really isn't a fix or a workaround!)

I don't know if it was because I am familiar with HTML or that I have gone through the nightmare that is NUS CS5223 Distributed Systems and I feel like I can survive anything now, but I managed to fix all my errors, yay! I have documented them in the section just above and I hope it makes life a little easier for anyone else who encounters them. A huge thank you goes out to all the amazingly helpful people on the net.

Also, my deployment of the Angular app to Github Pages isn't the most efficient way. But this seemed to be the only error-free one that I have found. I will keep searching for solutions in the meantime.

This is starting to read like an Oscars speech but this whole project reminded me of the days when I tinkered with the HTML on my Blogspot blog fervently and some day, when I need a wee bit of encouragement, I think this will do it. \(:
