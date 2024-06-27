import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  api_url = 'http://localhost:8000/get_answer';

  constructor(private http: HttpClient) { }

  getChatResponse(question: string) {
    const body = { question: question }; 
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    return this.http.put<any>(this.api_url, body, { headers: headers });
  }

  saveHistory(history: any){
    const historyString = JSON.stringify(history);
    localStorage.setItem('historialLabor', historyString);
  }
}
