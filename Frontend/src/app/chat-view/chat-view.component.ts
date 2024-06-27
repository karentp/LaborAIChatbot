import { Component } from '@angular/core';
import { ChatComponent } from '../chat/chat.component';
import { HeaderComponent } from '../header/header.component';

@Component({
  selector: 'app-chat-view',
  standalone: true,
  imports: [ChatComponent, HeaderComponent],
  templateUrl: './chat-view.component.html',
  styleUrl: './chat-view.component.css'
})
export class ChatViewComponent {

}
