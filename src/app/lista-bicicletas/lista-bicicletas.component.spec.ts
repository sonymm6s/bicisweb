import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaBicicletasComponent } from './lista-bicicletas.component';

describe('ListaBicicletasComponent', () => {
  let component: ListaBicicletasComponent;
  let fixture: ComponentFixture<ListaBicicletasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaBicicletasComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListaBicicletasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
