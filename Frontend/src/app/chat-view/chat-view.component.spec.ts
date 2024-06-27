import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChatViewComponent } from './chat-view.component';

describe('ChatViewComponent', () => {
  let component: ChatViewComponent;
  let fixture: ComponentFixture<ChatViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChatViewComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ChatViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
