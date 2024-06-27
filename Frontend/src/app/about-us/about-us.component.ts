import { Component } from '@angular/core';
import {HeaderComponent} from '../header/header.component'
import { RouterLink } from '@angular/router';


@Component({
  selector: 'app-about-us',
  standalone: true,
  imports: [HeaderComponent, RouterLink],
  templateUrl: './about-us.component.html',
  styleUrl: './about-us.component.css'
})
export class AboutUsComponent {

}
