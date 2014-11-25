#############################################################################
# Generated by PAGE version 4.3.1
# in conjunction with Tcl version 8.6
#    Nov 05, 2014 10:40:44 PM


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
#############################################################################
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Arial -size 11 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top36
    namespace eval ::widgets::$base {
        set set,origin 1
        set set,size 1
        set runvisible 1
    }
    set site_3_0 $base.fra52
    set site_3_0 $base.fra72
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow. {base} {
    if {$base == ""} {
        set base .
    }
    ###################
    # CREATING WIDGETS
    ###################
    wm focusmodel $top passive
    wm geometry $top 200x200+52+52; update
    wm maxsize $top 1276 773
    wm minsize $top 124 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm withdraw $top
    wm title $top "page"
    bindtags $top "$top Page all"
    ###################
    # SETTING GEOMETRY
    ###################

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top36 {base} {
    if {$base == ""} {
        set base .top36
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl:toplevel $top -class Toplevel \
        -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 284x242+440+192; update
    wm maxsize $top 1276 773
    wm minsize $top 124 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Camera Configuration"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    bindtags $top "$top Toplevel all _TopLevel"
    button $top.but39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Current 
    vTcl:DefineAlias "$top.but39" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but43 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Update Parameters} 
    vTcl:DefineAlias "$top.but43" "Button2" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che51 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -overrelief groove -relief groove -text All -variable check 
    vTcl:DefineAlias "$top.che51" "Checkbutton1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra52 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 25 \
        -width 95 
    vTcl:DefineAlias "$top.fra52" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra52
    label $site_3_0.lab53 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text Camera: 
    vTcl:DefineAlias "$site_3_0.lab53" "Label1" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_3_0.spi54 \
        -activebackground {#f9f9f9} -background white \
        -buttonbackground {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground black -from 1.0 -highlightbackground black \
        -highlightcolor black -increment 1.0 -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black \
        -textvariable spinbox -to 60.0 \
        -values {1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60} \
        -width 3 
    vTcl:DefineAlias "$site_3_0.spi54" "Spinbox1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab53 \
        -in $site_3_0 -x 4 -y 3 -width 47 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.spi54 \
        -in $site_3_0 -x 56 -y 5 -width 33 -height 19 -anchor nw \
        -bordermode ignore 
    frame $top.fra72 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 137 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 265 
    vTcl:DefineAlias "$top.fra72" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra72
    label $site_3_0.cpd73 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} -font font12 \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text ISO 
    vTcl:DefineAlias "$site_3_0.cpd73" "Label2" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.cpd76 \
        -values {6400 3200 1600 800 400 200} -textvariable ISO -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.cpd76" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.cpd78 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} -font font12 \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Aperature 
    vTcl:DefineAlias "$site_3_0.cpd78" "Label7" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.cpd79 \
        -values {6.4 5 4.5 4 3.2 1.7} -textvariable Aperature -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.cpd79" "TCombobox2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.cpd80 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} -font font12 \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Shutter Speed} 
    vTcl:DefineAlias "$site_3_0.cpd80" "Label4" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.cpd81 \
        -values {0.5 1/40 1/100 1/200 1/4000} -textvariable Speed \
        -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.cpd81" "TCombobox3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.cpd82 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} -font font12 \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Focus Mode} 
    vTcl:DefineAlias "$site_3_0.cpd82" "Label5" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.cpd83 \
        -values {{One Shot} {AI Servo} {AI Focus}} -textvariable Focus \
        -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.cpd83" "TCombobox4" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.cpd73 \
        -in $site_3_0 -x 10 -y 10 -anchor nw -bordermode inside 
    place $site_3_0.cpd76 \
        -in $site_3_0 -x 150 -y 10 -width 100 -anchor nw -bordermode inside 
    place $site_3_0.cpd78 \
        -in $site_3_0 -x 10 -y 40 -anchor nw -bordermode inside 
    place $site_3_0.cpd79 \
        -in $site_3_0 -x 150 -y 40 -width 100 -anchor nw -bordermode inside 
    place $site_3_0.cpd80 \
        -in $site_3_0 -x 10 -y 70 -anchor nw -bordermode inside 
    place $site_3_0.cpd81 \
        -in $site_3_0 -x 150 -y 70 -width 100 -anchor nw -bordermode inside 
    place $site_3_0.cpd82 \
        -in $site_3_0 -x 10 -y 100 -anchor nw -bordermode inside 
    place $site_3_0.cpd83 \
        -in $site_3_0 -x 150 -y 100 -width 100 -anchor nw -bordermode inside 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but39 \
        -in $top -x 170 -y 10 -width 102 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.but43 \
        -in $top -x 80 -y 200 -width 124 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.che51 \
        -in $top -x 110 -y 10 -width 52 -height 30 -anchor nw \
        -bordermode ignore 
    place $top.fra52 \
        -in $top -x 10 -y 10 -width 95 -height 30 -anchor nw \
        -bordermode ignore 
    place $top.fra72 \
        -in $top -x 10 -y 50 -width 265 -height 137 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top36
