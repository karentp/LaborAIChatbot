import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ChatViewComponent } from './chat-view/chat-view.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { TeamComponent } from './team/team.component';


export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'chat', component: ChatViewComponent},
    {path: 'about', component: AboutUsComponent},
    {path: 'team', component: TeamComponent}
];
