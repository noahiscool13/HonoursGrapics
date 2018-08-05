//
// Created by Noah Jadoenathmisier on 5-8-2018.
//


class Rectangle {
    int width, height;
public:
    void set_values (int,int);
    int area (void);
} rect;

class TTT {
    int bord[9] = {0,0,0,0,0,0,0,0,0};
public:
    void newBoard(){
        for (int i = 0; i<9; i++){
            bord[i] = 0;
        }
    }
};