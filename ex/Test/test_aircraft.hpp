#ifndef TEST_AIRCRAFT_HPP
#define TEST_AIRCRAFT_HPP

#include "test_aircraft.hpp"

#define  num_wp 6

#include "Task/TaskManager.hpp"


class AircraftSim {
public:
  AircraftSim(int _test_num);

  const AIRCRAFT_STATE& get_state() {
    return state;
  }
  GEOPOINT get_next() const;

  bool far();
  double small_rand();
  void update_state(TaskManager &task_manager,
                    GlidePolar &glide_polar);
  void integrate();

  bool advance(TaskManager &task_manager,
               GlidePolar &glide_polar);

#ifdef DO_PRINT
  void print(std::ostream &f4);
#endif
  double time();

private:
  AIRCRAFT_STATE state, state_last;
  GEOPOINT w[num_wp];
  double bearing;
  double sinkrate;
  int awp;
  int test_num;
  Filter heading_filt;

  enum AcState {
    Climb = 0,
    Cruise,
    FinalGlide
  };
  
  AcState acstate; 

};

#endif
