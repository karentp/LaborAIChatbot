import { Component } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { team } from './teamData';

@Component({
  selector: 'app-team',
  standalone: true,
  imports: [HeaderComponent],
  templateUrl: './team.component.html',
  styleUrl: './team.component.css'
})
export class TeamComponent {
 teamMembers = team;
}
