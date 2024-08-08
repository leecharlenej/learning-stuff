import { Injectable } from '@angular/core';
import { Project } from '../_modals/project';
import { Tag } from '../_modals/tag';

@Injectable({
  providedIn: 'root'
})
export class ProjectsService {

  projects: Project[] = [
    {id: 0, name: "HDB Price Prediction", pictures: ["/img/image1.png","/img/image2.png","/img/image3.png"], projectLink: "//github.com/leecharlenej/fuzzy-eureka", summary: "Python project for data analytics on Singapore's HDB prices.", description: "This is a group NUS school project, under the module IT5006 Fundamentals of Data Analytics. A Streamlit app was developed to analyze the prices of resale and rental houses in Singapore. Various models such as random forest regression, linear regression and XGBoost were implement to identify the best predictive model.", tags: [Tag.PYTHON]},
    {id: 1, name: "Distributed Systems Project", pictures: ["/img/image1.png","/img/image2.png","/img/image3.png"], projectLink: "//www.github.com", summary: "Java project to build a linearizable, sharded key-value store.", description: "This is a NUS school project, under the module CS5223 Distributed Systems. There are 5 labs, each focusing on different aspects of distributed systems such as remote procedure calls, key-value store replication, Paxos consensus, sharding, and dynamic load balancing. It is similar to Amazon\'s DynamoDB or Google\'s Spanner. As this project is still being used at NUS, please contact me for the link.", tags: [Tag.JAVA]},
    {id: 2, name: "MCQ Quiz Generator", pictures: ["/img/projects/python-mcq-quiz-generator/image1.png","/img/projects/python-mcq-quiz-generator/image2.png","/img/projects/python-mcq-quiz-generator/image3.png"], projectLink: "//github.com/leecharlenej/mcq-quiz-generator", summary: "Python project that generates a MCQ quiz in Word.", description: "The MCQ Quiz Generator is a versatile tool crafted to assist educators and examiners in creating, modifying, and randomizing fact-based multiple-choice questions (MCQs) to ensure a varied testing experience. This innovative tool integrates ChatGPT to dynamically rephrase existing questions or to generate new ones, consistently testing the same concepts through varied phrasing.", tags: [Tag.PYTHON]},
    {id: 4, name: "Angular Portfolio", pictures: ["/img/image1.png","/img/image2.png","/img/image3.png"], projectLink: "//github.com/leecharlenej/learning-stuff/tree/master/Web-app/AngularPortfolioWebsite2", summary: "Angular project to house my porfolio.", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", tags: [Tag.ANGULAR]},
    {id: 5, name: "Coding Practices", pictures: ["/img/image1.png","/img/image2.png","/img/image3.png"], projectLink: "//github.com/leecharlenej/coding-practices", summary: "Web API Project that was developed for a class project.", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", tags: [Tag.PYTHON]},
    {id: 6, name: "The Odin Project", pictures: ["/img/image1.png","/img/image2.png","/img/image3.png"], projectLink: "//www.github.com", summary: "Mobile app developed in java that tracks the departure and arrival of trains.", description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", tags: [Tag.JAVASCRIPT, Tag.JAVA]}
  ];
  
  constructor() { }

  GetProjects(){
    return this.projects;
  }

  GetProjectById(id: number): Project {
    let project = this.projects.find( project => project.id === id)

    if (project === undefined) {
      throw new TypeError('There is no project that matches the id: ' + id)
    }

    return project;
  }

  GetProjectsByFilter(filterTags: Tag[]){
    let filteredProjects: Project[] = [];

    this.projects.forEach(function (project) {
      let foundAll = true;

      filterTags.forEach(function (filterTags) {
        if (project.tags.includes(filterTags)==false){
          foundAll = false;
        }

      });

      if (foundAll) {
        filteredProjects.push(project);
      }


    });
    return filteredProjects;
  }
}
