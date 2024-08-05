# Setting up environment
1. Check version: `ng version`
- Error: `\npm\ng.ps1 cannot be loaded because running scripts is disabled on this system.`
- Solution: Go to `C:\Users\{user_name}\AppData\Roaming\npm`. Delete `ng.ps1`

2. Installation: Go to folder > `ng new`
- `Do you want to enable Server-Side Rendering (SSR) and Static Site Generation (SSG/Prerendering)? no` for single-page application
- `ng new my-app --no-standalone --routing --ssr=false`: To have app.module.ts

# Installed files

1. `src/index.html`
- Contains whole website.
- approot: Entry point for Angular app.

2. `src/app/app.component.html`
- Contains CSS and HTML code that is displayed on webpage.

3. Build project: Right-click on project. > Select `Open in Integrated Terminal`. > `ng serve`

4. Angular components (3): Build different sections of the website.
- `src/app/app/app.component.ts`: Add functionality to component.
- `src/app/app/app.component.html`: HTML template
- `src/app/app/app.component.css`: Associate style sheet for the component. vs `styles.css`: Defined globally
- `{{}}`: Insert data from varaible in component file into HTML.
- `selector`: Use to identify diffferent components.
> -`index.html`: `<app-root></app-root>` points to `app.component.ts`: `selector: 'app-root'`