#include <iostream>
 
using namespace std;

// Base class
class Building {
    public:
        void set_square_footage(int sf) {
            square_footage = sf;
        }
        void set_location_latitude(float lat) {
            latitude = lat;
        }
        void set_location_longitude(float loc_longitude) {
            longitude = loc_longitude;
        }
    protected:
        int square_footage;
        float latitude;
        float longitude;
};


