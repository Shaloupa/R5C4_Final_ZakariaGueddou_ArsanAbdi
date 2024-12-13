import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
  searches: any[] = [];
  page: number = 1;
  limit: number = 30;
  total: number = 0;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadPage();
  }

  loadPage(): void {
    this.http.get<any>(`http://127.0.0.1:5000/searches?page=${this.page}&limit=${this.limit}`)
      .subscribe(data => {
        this.searches = data.data;
        this.total = data.total;
      });
  }

  nextPage(): void {
    if (this.page * this.limit < this.total) {
      this.page++;
      this.loadPage();
    }
  }

  prevPage(): void {
    if (this.page > 1) {
      this.page--;
      this.loadPage();
    }
  }
}
