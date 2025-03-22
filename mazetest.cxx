#include <FL/Fl.H>
#include <FL/Fl_Double_Window.H>
#include <FL/Fl_Box.H>
#include <FL/fl_draw.H>
#include <string>
#include <cmath>
#include <cstdlib>

#ifdef _WIN32
    #include <windows.h>  // For SetCursorPos on Windows
#endif

using namespace std;

namespace common {
    float px = 60.0;
    float py = 60.0;
    float pdir = 0.0;

    int pensize = 1;
    float ray_y = 400;
    float ray_x = 0;

    const float cellsize = 40;

    constexpr const char* maze[40] = {
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X   X   X       X           X         XX",
        "XXX X XXX X XXX XXXXXXXXX X X XXXXXXX XX",
        "X   X     X X X           X   X       XX",
        "X XXXXXXXXX X XXXXXXXXXXXXXXXXX XXXXXXXX",
        "X     X   X X           X     X       XX",
        "XXXXX X X X X XXXXX XXX X X X XXXXXXX XX",
        "X   X   X   X   X   X   X X X X   X   XX",
        "X X XXXXXXXXXXXXX XXXXXXX X X X X X XXXX",
        "X X     X         X       X X X X   X XX",
        "XXXXX X X X XXXXXXX XXXXXXX X X XXXXX XX",
        "X     X   X X   X       X   X X X     XX",
        "X XXXXXXXXX X X X XXXXXXX XXX X XXXXX XX",
        "X       X   X X   X       X   X       XX",
        "X XXXXX X XXX XXXXX XXXXXXX XXXXXXXXX XX",
        "X     X X   X   X X X       X     X   XX",
        "XXXXXXX XXX XXX X X X XXXXXXX X XXX XXXX",
        "X       X     X   X X   X   X X   X   XX",
        "X XXXXX XXXXXXXXX X XXX X X XXXXX XXX XX",
        "X X     X   X     X X X X X       X X XX",
        "X XXX XXX X X XXXXX   X X XXXXXXX X X XX",
        "X   X X   X     X   X X X X         X XX",
        "X X X X XXXXXXXXX XXX X X X XXXXXXXXX XX",
        "X X X X   X       X       X     X     XX",
        "X X XXX XXX XXXXXXX XXXXXXXXXXX X XXXXXX",
        "X X   X X   X     X   X       X X     XX",
        "X XXX X X XXXXX X X XXX XXXXX X XXXXX XX",
        "X X X X X     X X   X   X   X X     X XX",
        "X X X X XXXXX XXXXXXX XXX X X XXXXXXX XX",
        "X   X   X   X         X   X X X       XX",
        "XXX XXXXXXX XXXXXXXXXXX XXX X X XXXXXXXX",
        "X X     X   X     X     X   X X X     XX",
        "X XXXXX X XXX X XXX XXXXX XXX X XXX X XX",
        "X     X X     X   X   X       X   X X XX",
        "X X XXX XXXXXXXXX XXX X XXXXXXXXX X X XX",
        "X X   X X       X   X X   X     X X X XX",
        "X XXX X X XXXXX X X X XXXXX X XXX XXX XX",
        "X   X     X       X X       X         XX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    };
    

    int px_to_ref(float val){
        return int(val)/40; // TODO
    }
}

void pmove(float &px, float &py, float dir, float dist){
    double inrad = dir * M_PI / 180.0;

    float dx = dist * cos(inrad);
    float dy = dist * sin(inrad);

    if((common::maze[common::px_to_ref(py+dy)][common::px_to_ref(px+dx)])==' '){
        px += dx;
        py += dy;
    }
}

void raymaster(float w, float h){
    common::ray_x = -w/2;
    for(;common::ray_x<((w/common::pensize)+1);common::ray_x+=common::pensize){
        float rx = common::px;
        float ry = common::py;
        float rdir = (atan2(common::ray_x, common::ray_y) * (180.0 / M_PI))+common::pdir;
        double inrad = rdir * M_PI / 180.0;
        float dx = cos(inrad);
        float dy = sin(inrad);
        while((common::maze[common::px_to_ref(ry)][common::px_to_ref(rx)])==' '){
            rx += dx * 5.0;
            ry += dy * 5.0;
        }
        while((common::maze[common::px_to_ref(ry)][common::px_to_ref(rx)])=='X'){
            rx += dx * -1.0;
            ry += dy * -1.0;
        }
        float dist = hypot(rx - common::px, ry - common::py) * cos((rdir - common::pdir)*(M_PI/180.0));
        float scale = common::ray_y / dist;
        fl_color(FL_WHITE);
        fl_line(common::ray_x+w/2, (-20*scale)+h/2, common::ray_x+w/2, (20*scale)+h/2);
    }
}

class Canvas : public Fl_Box {
    public:
        Canvas(int X, int Y, int W, int H, const char*L=0) : Fl_Box(X,Y,W,H,L){};

        void draw(){
            fl_color(FL_BLACK);
            fl_rectf(0, 0, w(), h());
            fl_line_style(FL_SOLID|FL_CAP_ROUND|FL_JOIN_ROUND, common::pensize);
            raymaster(w(), h());
        }
};


class GWindow : public Fl_Double_Window {
    public:

        int center_x, center_y;
        bool is_full = false;

        GWindow(int w, int h, const char* title = 0) : Fl_Double_Window(w, h, title) {
            center_x = w / 2;
            center_y = h / 2;
        }

        int handle(int event) override {
            if (event == FL_KEYDOWN) {
                int key = Fl::event_key();
                switch (key) { 
                    case 'w': pmove(common::px, common::py, common::pdir, 5.0); break;
                    case 's': pmove(common::px, common::py, common::pdir, -5.0); break;
                    case 'f': if(!is_full){
                                this->fullscreen();is_full=true;
                              }else{
                                this->fullscreen_off();is_full=false;
                              }; break;
                    case 'q': Fl::delete_widget(this); exit(0);
                    default: break;
                }
                // cout << common::px << " " << common::py << " " << common::pdir << endl;
                return 1;
            }else if(event == FL_MOVE){
                int mx = Fl::event_x();
                common::pdir += mx - center_x;
                int my = Fl::event_y();

                // Re-center mouse if it moves away from the center
                if (mx != center_x || my != center_y) {
                    warp_mouse(center_x, center_y);
                }
                return 1;
            }
            return Fl_Window::handle(event);
        }
        
        void warp_mouse(int x, int y) {
            #ifdef _WIN32
                POINT p;
                ClientToScreen(fl_xid(this), &p);  // Get window position on screen
                SetCursorPos(p.x + x, p.y + y);
            #else
                XWarpPointer(fl_display, None, fl_window, 0, 0, 0, 0, x, y);
                XFlush(fl_display);
            #endif
        }
        
};

void eventLoop(void* datum){
    if (!datum) return;  // Ensure `datum` is valid.
    Canvas* cvp = (Canvas*)datum;
    
    // TODO

    cvp->damage(1);
    Fl::repeat_timeout(0.016, eventLoop, cvp);
} 

int main(int argc, char** argv){
    Fl::visual(FL_DOUBLE|FL_INDEX);
    GWindow TestWindow(480, 360, "Maze");
    Canvas TestCanvas(0, 0, TestWindow.w(), TestWindow.h());
    Canvas* cv = &TestCanvas;
    Fl::add_timeout(0.016, eventLoop, cv);
    TestWindow.resizable(TestCanvas);
    TestWindow.show();
    return(Fl::run());
}