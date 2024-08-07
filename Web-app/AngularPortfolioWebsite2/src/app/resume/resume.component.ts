import { Component, Renderer2 } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-resume',
  templateUrl: './resume.component.html',
  styleUrl: './resume.component.css'
})
export class ResumeComponent {
  

  isWorkExperienceOpen: boolean = false;
  isEducationOpen: boolean = false;
  isCertificationsOpen: boolean = false;
  isSkillsOpen: boolean = false;

  constructor(private titleService: Title, private renderer: Renderer2) {
    this.titleService.setTitle('Charlene L. - Resume');
   }

   DownloadFile(){
    const link = this.renderer.createElement('a');
    link.setAttribute('target', '_link');
    link.setAttribute('href', '2024_resume_charlene.pdf');
    link.setAttribute('download', '2024_resume_charlene.pdf');
    link.click();
    link.remove();
   }

}
