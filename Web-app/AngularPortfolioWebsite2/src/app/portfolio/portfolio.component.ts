import { Component } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Project } from '../_modals/project';
import { Tag } from '../_modals/tag';

@Component({
  selector: 'app-portfolio',
  templateUrl: './portfolio.component.html',
  styleUrl: './portfolio.component.css'
})
export class PortfolioComponent {

  project: Project = {
    id: 0,
    name: 'Single Angular App',
    summary: 'Test description',
    description: '',
    projectlink: '',
    pictures: [],
    tags: [Tag.ANGULAR, Tag.TYPESCRIPT],
  }
  
  constructor(private titleService: Title) {
    this.titleService.setTitle('Charlene L. - Portfolio');
   }

}
