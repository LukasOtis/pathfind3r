#dataflow within pathfind3r

```
     GCODE
       |
       |
       v
   gcodeparser
*returns array of [x,y,z]*
       |
       |
       v
     grid
*returns array of timed steps [0, 1]*
       |
       |
       v
  motor controller
*executes commands on different motors in right order*
      /|\
     / | \
    /  |  \
   v   v   v 
     motors

```
