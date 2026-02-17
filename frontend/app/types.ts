export interface TicketItem {
    id: number;
    price: number;
    quantity: number;
    sections: string;
    sector: string;
    row: string;
    seat: string;
    notes: string;
}
export interface TicketEvent {
    id: number;
    title: string;
    place: string;
    city: string;
    start_datetime: string;
    end_datetime: string;
    ticket_items: TicketItem[];
}


