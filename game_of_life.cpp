#include <gtkmm.h>

#define XSPAN 150
#define YSPAN 150

using namespace std;

class LifeWindow : public Gtk::Window {
    public:
        LifeWindow();
        Gtk::Grid LifeDisplayRoot;
        Gtk::ScrolledWindow LifeLand;
        Gtk::Grid LifeDisplay;
        Gtk::ToggleButton LifeCells[XSPAN*YSPAN];
        Gtk::Button LifeRunner;
        bool isLife = false;
        sigc::connection LifeConnection;
        void LifeDoLoop();
        bool LifeLoop();
        void LifeExecuter();
        int LifeNeighbours(int);
};

LifeWindow::LifeWindow() : LifeRunner("Play"){
    set_title("Conway's Game Of Life");
    set_default_size(500, 500);
    
    set_child(LifeDisplayRoot);

    LifeDisplayRoot.attach(LifeRunner, 0, 0);
    LifeDisplayRoot.attach(LifeLand, 0, 1);
    
    LifeLand.set_child(LifeDisplay);

    LifeDisplay.set_margin(25);
    LifeDisplay.set_halign(Gtk::Align::CENTER);
    int xpos = 0;
    int ypos = 0;
    for(int i=0;ypos<YSPAN;i++){
        LifeDisplay.attach(LifeCells[i], xpos, ypos);
        xpos++;
        if(xpos==XSPAN){ypos++;xpos=0;}
    }
    LifeRunner.set_size_request(1800, 25);
    LifeLand.set_size_request(1800, 1000);
    LifeRunner.signal_clicked().connect(sigc::mem_fun(*this, &LifeWindow::LifeDoLoop));
}

int LifeWindow::LifeNeighbours(int place){
    int amt = 0;

    if(place<XSPAN){}
    else{
        if(LifeCells[place-XSPAN-1].get_active()){amt++;}
        if(LifeCells[place-XSPAN].get_active()){amt++;}
        if(LifeCells[place-XSPAN+1].get_active()){amt++;}
    }

    if(place % XSPAN == 0){}
    else{
        if(LifeCells[place-1].get_active()){amt++;}
    }

    if(place % XSPAN == (XSPAN - 1)){}
    else{
        if(LifeCells[place+1].get_active()){amt++;}
    }

    if(place >= ((XSPAN*YSPAN)-XSPAN)){}
    else{
        if(LifeCells[place+XSPAN-1].get_active()){amt++;}
        if(LifeCells[place+XSPAN].get_active()){amt++;}
        if(LifeCells[place+XSPAN+1].get_active()){amt++;}
    }
    return amt;
}

void LifeWindow::LifeDoLoop(){
    if(!isLife){
        LifeConnection = Glib::signal_timeout().connect(sigc::mem_fun(*this, &LifeWindow::LifeLoop), 100);
        isLife = true;
    } else {
        LifeConnection.disconnect();
        isLife = false;
    }
}

bool LifeWindow::LifeLoop(){
    LifeWindow::LifeExecuter();
    return true;
}

void LifeWindow::LifeExecuter(){
    bool results[XSPAN*YSPAN];
    for(int i=0;i<XSPAN*YSPAN;i++){
        if(LifeCells[i].get_active()){
            if((LifeNeighbours(i)==2)||(LifeNeighbours(i)==3)){
                results[i] = true;
            } 
            else {
                results[i] = false;
            }
        } 
        else {
            if(LifeNeighbours(i)==3){
                results[i] = true;
            } 
            else {
                results[i] = false;
            }
        }
    }
    for(int j=0;j<XSPAN*YSPAN;j++){
        LifeCells[j].set_active(results[j]);
    }
    
}

int main(int argc, char* argv[]){
    auto app = Gtk::Application::create("");
    return app->make_window_and_run<LifeWindow>(argc, argv);
}
