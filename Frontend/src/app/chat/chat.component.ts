import { Component, OnInit } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { ChatService } from '../services/chat.service';
import { CommonModule, NgClass } from '@angular/common';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [FormsModule, NgClass, CommonModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  chatHistory: {type: string, text: string, timestamp: Date, context?: string[]}[] = [];

  constructor(private chatService: ChatService){}
  
  ngOnInit(): void {
    const history = localStorage.getItem('historialLabor');
    if(history){
      this.chatHistory = JSON.parse(history);
    }
  }

  onSubmit(formData: NgForm){
    const question = formData.form.value.question;
    if (!question) return;  // Verificar que la pregunta no esté vacía

    const cleanQuestion = this.cleanQuestion(question);
    console.log(cleanQuestion);
    const questionEntry = {type: 'user', text: question, timestamp: new Date()};
    this.chatHistory.push(questionEntry);
    
    this.chatService.getChatResponse(question).subscribe(response => {
      console.log(response);
      const responseEntry = {type: 'bot', text: response.answer, timestamp: new Date(), context: response.context};
      this.chatHistory.push(responseEntry);
      this.chatService.saveHistory(this.chatHistory);
    });
    
    formData.reset();  // Limpiar el formulario después de enviar
  }

  cleanQuestion(question: string): string {
    const normalizedQuestion = question.toLowerCase();
    return normalizedQuestion.replace(/[^\w\s]/gi, ' ');
  }

  extractArticles(text: string): string[] {
    const articleRegex = /ARTICULO\s+\d+/gi;
    return text.match(articleRegex) || [];
  }

  clearChat() {
    this.chatHistory = [];
    localStorage.removeItem('historialLabor');
  }
}
