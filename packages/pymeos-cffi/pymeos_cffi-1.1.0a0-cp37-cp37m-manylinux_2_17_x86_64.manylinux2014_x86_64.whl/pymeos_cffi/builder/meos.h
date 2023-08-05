/*****************************************************************************
 *
 * This MobilityDB code is provided under The PostgreSQL License.
 * Copyright (c) 2016-2023, Université libre de Bruxelles and MobilityDB
 * contributors
 *
 * MobilityDB includes portions of PostGIS version 3 source code released
 * under the GNU General Public License (GPLv2 or later).
 * Copyright (c) 2001-2023, PostGIS contributors
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose, without fee, and without a written
 * agreement is hereby granted, provided that the above copyright notice and
 * this paragraph and the following two paragraphs appear in all copies.
 *
 * IN NO EVENT SHALL UNIVERSITE LIBRE DE BRUXELLES BE LIABLE TO ANY PARTY FOR
 * DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING
 * LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,
 * EVEN IF UNIVERSITE LIBRE DE BRUXELLES HAS BEEN ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGE.
 *
 * UNIVERSITE LIBRE DE BRUXELLES SPECIFICALLY DISCLAIMS ANY WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
 * AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON
 * AN "AS IS" BASIS, AND UNIVERSITE LIBRE DE BRUXELLES HAS NO OBLIGATIONS TO
 * PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS. 
 *
 *****************************************************************************/

/**
 * @brief API of the Mobility Engine Open Source (MEOS) library.
 */

//#ifndef __MEOS_H__
//#define __MEOS_H__


//#include <stdbool.h>
//#include <stdint.h>

//#ifndef POSTGRES_H
//#define POSTGRES_H

typedef uintptr_t Datum;

typedef signed char int8;
typedef signed short int16;
typedef signed int int32;
typedef long int int64;

typedef unsigned char uint8;
typedef unsigned short uint16;
typedef unsigned int uint32;
typedef unsigned long int uint64;

typedef int32 DateADT;
typedef int64 TimeADT;
typedef int64 Timestamp;
typedef int64 TimestampTz;
typedef int64 TimeOffset;
typedef int32 fsec_t;      

typedef struct
{
  TimeOffset time;  
  int32 day;        
  int32 month;      
} Interval;

typedef struct varlena
{
  char vl_len_[4];  
  char vl_dat[];    
} varlena;

typedef varlena text;
typedef struct varlena bytea;

//#endif              


//#ifndef _LIBLWGEOM_H
//#define _LIBLWGEOM_H



/*
** Variants available for WKB and WKT output types
*/

//#define WKB_ISO 0x01
//#define WKB_SFSQL 0x02
//#define WKB_EXTENDED 0x04
//#define WKB_NDR 0x08
//#define WKB_XDR 0x10
//#define WKB_HEX 0x20
//#define WKB_NO_NPOINTS 0x40 
//#define WKB_NO_SRID 0x80 

//#define WKT_ISO 0x01
//#define WKT_SFSQL 0x02
//#define WKT_EXTENDED 0x04

typedef uint16_t lwflags_t;



typedef struct {
    double afac, bfac, cfac, dfac, efac, ffac, gfac, hfac, ifac, xoff, yoff, zoff;
} AFFINE;



typedef struct
{
    double xmin, ymin, zmin;
    double xmax, ymax, zmax;
    int32_t srid;
}
BOX3D;

/******************************************************************
* GBOX structure.
* We include the flags (information about dimensionality),
* so we don't have to constantly pass them
* into functions that use the GBOX.
*/
typedef struct
{
    lwflags_t flags;
    double xmin;
    double xmax;
    double ymin;
    double ymax;
    double zmin;
    double zmax;
    double mmin;
    double mmax;
} GBOX;


/******************************************************************
* SPHEROID
*
*  Standard definition of an ellipsoid (what wkt calls a spheroid)
*    f = (a-b)/a
*    e_sq = (a*a - b*b)/(a*a)
*    b = a - fa
*/
typedef struct
{
    double  a;  
    double  b;  
    double  f;  
    double  e;  
    double  e_sq;   
    double  radius;  
    char    name[20];  
}
SPHEROID;

/******************************************************************
* POINT2D, POINT3D, POINT3DM, POINT4D
*/
typedef struct
{
    double x, y;
}
POINT2D;

typedef struct
{
    double x, y, z;
}
POINT3DZ;

typedef struct
{
    double x, y, z;
}
POINT3D;

typedef struct
{
    double x, y, m;
}
POINT3DM;

typedef struct
{
    double x, y, z, m;
}
POINT4D;

/******************************************************************
*  POINTARRAY
*  Point array abstracts a lot of the complexity of points and point lists.
*  It handles 2d/3d translation
*    (2d points converted to 3d will have z=0 or NaN)
*  DO NOT MIX 2D and 3D POINTS! EVERYTHING* is either one or the other
*/
typedef struct
{
    uint32_t npoints;   
    uint32_t maxpoints; 

    
    lwflags_t flags;

    
    uint8_t *serialized_pointlist;
}
POINTARRAY;

/******************************************************************
* GSERIALIZED
*/

typedef struct
{
    uint32_t size; 
    uint8_t srid[3]; 
    uint8_t gflags; 
    uint8_t data[1]; 
} GSERIALIZED;

/******************************************************************
* LWGEOM (any geometry type)
*
* Abstract type, note that 'type', 'bbox' and 'srid' are available in
* all geometry variants.
*/
typedef struct
{
    GBOX *bbox;
    void *data;
    int32_t srid;
    lwflags_t flags;
    uint8_t type;
    char pad[1]; 
}
LWGEOM;


typedef struct
{
    GBOX *bbox;
    POINTARRAY *point;  
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
}
LWPOINT; 


typedef struct
{
    GBOX *bbox;
    POINTARRAY *points; 
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
}
LWLINE; 


typedef struct
{
    GBOX *bbox;
    POINTARRAY *points;
    int32_t srid;
    lwflags_t flags;
    uint8_t type;
    char pad[1]; 
}
LWTRIANGLE;


typedef struct
{
    GBOX *bbox;
    POINTARRAY *points; 
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
}
LWCIRCSTRING; 


typedef struct
{
    GBOX *bbox;
    POINTARRAY **rings; 
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t nrings;   
    uint32_t maxrings; 
}
LWPOLY; 


typedef struct
{
    GBOX *bbox;
    LWPOINT **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWMPOINT;


typedef struct
{
    GBOX *bbox;
    LWLINE **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWMLINE;


typedef struct
{
    GBOX *bbox;
    LWPOLY **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWMPOLY;


typedef struct
{
    GBOX *bbox;
    LWGEOM **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWCOLLECTION;


typedef struct
{
    GBOX *bbox;
    LWGEOM **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWCOMPOUND; 


typedef struct
{
    GBOX *bbox;
    LWGEOM **rings;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t nrings;    
    uint32_t maxrings;  
}
LWCURVEPOLY; 


typedef struct
{
    GBOX *bbox;
    LWGEOM **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWMCURVE;


typedef struct
{
    GBOX *bbox;
    LWGEOM **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWMSURFACE;


typedef struct
{
    GBOX *bbox;
    LWPOLY **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWPSURFACE;


typedef struct
{
    GBOX *bbox;
    LWTRIANGLE **geoms;
    int32_t srid;
    lwflags_t flags;
    uint8_t type; 
    char pad[1]; 
    uint32_t ngeoms;   
    uint32_t maxgeoms; 
}
LWTIN;

extern LWPOINT *lwpoint_make(int32_t srid, int hasz, int hasm, const POINT4D *p);

extern LWGEOM *lwgeom_from_gserialized(const GSERIALIZED *g);
extern GSERIALIZED *gserialized_from_lwgeom(LWGEOM *geom, size_t *size);



extern int32_t lwgeom_get_srid(const LWGEOM *geom);

extern double lwpoint_get_x(const LWPOINT *point);
extern double lwpoint_get_y(const LWPOINT *point);
extern double lwpoint_get_z(const LWPOINT *point);
extern double lwpoint_get_m(const LWPOINT *point);

extern int lwgeom_has_z(const LWGEOM *geom);
extern int lwgeom_has_m(const LWGEOM *geom);

//#endif              



/*****************************************************************************
 * Type definitions
 *****************************************************************************/

/**
 * @brief Align to double
 */
//#define DOUBLE_PAD(size) ( (size) + ((size) % 8 ? (8 - (size) % 8) : 0 ) )

/**
 * Structure to represent sets of values
 */
typedef struct
{
  int32 vl_len_;        
  uint8 settype;        
  uint8 basetype;       
  int16 flags;          
  int32 count;          
  int32 maxcount;       
  int32 bboxsize;       
} Set;

/**
 * Structure to represent spans (a.k.a. ranges)
 */
typedef struct
{
  uint8 spantype;       
  uint8 basetype;       
  bool lower_inc;       
  bool upper_inc;       
  Datum lower;          
  Datum upper;          
} Span;

/**
 * Structure to represent span sets
 */
typedef struct
{
  int32 vl_len_;        
  uint8 spansettype;    
  uint8 spantype;       
  uint8 basetype;       
  char padding;         
  int32 count;          
  int32 maxcount;       
  Span span;            
  Span elems[1];        
} SpanSet;

/**
 * Structure to represent temporal boxes
 */
typedef struct
{
  Span period;          
  Span span;            
  int16 flags;          
} TBox;

/**
 * Structure to represent spatiotemporal boxes
 */
typedef struct
{
  Span period;          
  double xmin;          
  double xmax;          
  double ymin;          
  double ymax;          
  double zmin;          
  double zmax;          
  int32  srid;          
  int16  flags;         
} STBox;

/**
 * @brief Enumeration that defines the interpolation types used in
 * MobilityDB.
 */
typedef enum
{
  INTERP_NONE =    0,
  DISCRETE =       1,
  STEP =           2,
  LINEAR =         3,
} interpType;

/**
 * Structure to represent the common structure of temporal values of
 * any temporal subtype
 */
typedef struct
{
  int32 vl_len_;        
  uint8 temptype;       
  uint8 subtype;        
  int16 flags;          
  
} Temporal;

/**
 * Structure to represent temporal values of instant subtype
 */
typedef struct
{
  int32 vl_len_;        
  uint8 temptype;       
  uint8 subtype;        
  int16 flags;          
  TimestampTz t;        
  Datum value;          /**< Base value for types passed by value,
                             first 8 bytes of the base value for values
                             passed by reference. The extra bytes
                             needed are added upon creation. */
  
} TInstant;

/**
 * Structure to represent temporal values of instant set or sequence subtype
 */
typedef struct
{
  int32 vl_len_;        
  uint8 temptype;       
  uint8 subtype;        
  int16 flags;          
  int32 count;          
  int32 maxcount;       
  int16 bboxsize;       
  char padding[6];      
  Span period;          /**< Time span (24 bytes). All bounding boxes start
                             with a period so actually it is also the begining
                             of the bounding box. The extra bytes needed for
                             the bounding box are added upon creation. */
  
} TSequence;

//#define TSEQUENCE_BBOX_PTR(seq)      ((void *)(&(seq)->period))

/**
 * Structure to represent temporal values of sequence set subtype
 */
typedef struct
{
  int32 vl_len_;        
  uint8 temptype;       
  uint8 subtype;        
  int16 flags;          
  int32 count;          
  int32 totalcount;     /**< Total number of TInstant elements in all
                             composing TSequence elements */
  int32 maxcount;       
  int16 bboxsize;       
  int16 padding;        
  Span period;          /**< Time span (24 bytes). All bounding boxes start
                             with a period so actually it is also the begining
                             of the bounding box. The extra bytes needed for
                             the bounding box are added upon creation. */
  
} TSequenceSet;

//#define TSEQUENCESET_BBOX_PTR(ss)      ((void *)(&(ss)->period))

/**
 * Struct for storing a similarity match
 */
typedef struct
{
  int i;
  int j;
} Match;



/**
 * Structure to represent skiplist elements
 */

#define SKIPLIST_MAXLEVEL 32
typedef struct
{
  void *value;
  int height;
  int next[SKIPLIST_MAXLEVEL];
} SkipListElem;

/**
 * Structure to represent skiplists that keep the current state of an aggregation
 */
typedef struct
{
  int capacity;
  int next;
  int length;
  int *freed;
  int freecount;
  int freecap;
  int tail;
  void *extra;
  size_t extrasize;
  SkipListElem *elems;
} SkipList;

/*****************************************************************************
 * Initialization of the MEOS library
 *****************************************************************************/

extern void meos_initialize(const char *tz_str);
extern void meos_finalize(void);

/*****************************************************************************
 * Functions for input/output PostgreSQL time types
 *****************************************************************************/

extern bool bool_in(const char *in_str);
extern char *bool_out(bool b);
extern DateADT pg_date_in(const char *str);
extern char *pg_date_out(DateADT date);
extern int pg_interval_cmp(const Interval *interval1, const Interval *interval2);
extern Interval *pg_interval_in(const char *str, int32 typmod);
extern Interval *pg_interval_make(int32 years, int32 months, int32 weeks, int32 days, int32 hours, int32 mins, double secs);
extern Interval *pg_interval_mul(const Interval *span, double factor);
extern char *pg_interval_out(const Interval *span);
extern Interval *pg_interval_pl(const Interval *span1, const Interval *span2);
extern TimeADT pg_time_in(const char *str, int32 typmod);
extern char *pg_time_out(TimeADT time);
extern Timestamp pg_timestamp_in(const char *str, int32 typmod);
extern Interval *pg_timestamp_mi(TimestampTz dt1, TimestampTz dt2);
extern TimestampTz pg_timestamp_mi_interval(TimestampTz timestamp, const Interval *span);
extern char *pg_timestamp_out(Timestamp dt);
extern TimestampTz pg_timestamp_pl_interval(TimestampTz timestamp, const Interval *span);
extern TimestampTz pg_timestamptz_in(const char *str, int32 typmod);
extern char *pg_timestamptz_out(TimestampTz dt);

/*****************************************************************************
 * Functions for input/output and manipulation of PostGIS types
 *****************************************************************************/

extern bytea *gserialized_as_ewkb(const GSERIALIZED *geom, char *type);
extern char *gserialized_as_ewkt(const GSERIALIZED *geom, int precision);
extern char *gserialized_as_geojson(const GSERIALIZED *geom, int option, int precision, char *srs);
extern char *gserialized_as_hexewkb(const GSERIALIZED *geom, const char *type);
extern char *gserialized_as_text(const GSERIALIZED *geom, int precision);
extern GSERIALIZED *gserialized_from_ewkb(const bytea *bytea_wkb, int32 srid);
extern GSERIALIZED *gserialized_from_geojson(const char *geojson);
extern GSERIALIZED *gserialized_from_hexewkb(const char *wkt);
extern GSERIALIZED *gserialized_from_text(char *wkt, int srid);
extern GSERIALIZED *gserialized_in(char *input, int32 geom_typmod);
extern char *gserialized_out(const GSERIALIZED *geom);
extern bool pgis_gserialized_same(const GSERIALIZED *geom1, const GSERIALIZED *geom2);

/*****************************************************************************
 * Functions for set and span types
 *****************************************************************************/



extern Set *bigintset_in(const char *str);
extern char *bigintset_out(const Set *set);
extern Span *bigintspan_in(const char *str);
extern char *bigintspan_out(const Span *s);
extern SpanSet *bigintspanset_in(const char *str);
extern char *bigintspanset_out(const SpanSet *ss);
extern Set *floatset_in(const char *str);
extern char *floatset_out(const Set *set, int maxdd);
extern Span *floatspan_in(const char *str);
extern char *floatspan_out(const Span *s, int maxdd);
extern SpanSet *floatspanset_in(const char *str);
extern char *floatspanset_out(const SpanSet *ss, int maxdd);
extern char *geogset_out(const Set *set, int maxdd);
extern char *geomset_out(const Set *set, int maxdd);
extern char *geoset_as_text(const Set *set, int maxdd);
extern char *geoset_as_ewkt(const Set *set, int maxdd);
extern Set *intset_in(const char *str);
extern char *intset_out(const Set *set);
extern Span *intspan_in(const char *str);
extern char *intspan_out(const Span *s);
extern SpanSet *intspanset_in(const char *str);
extern char *intspanset_out(const SpanSet *ss);

extern Span *period_in(const char *str);
extern char *period_out(const Span *s);
extern SpanSet *periodset_in(const char *str);
extern char *periodset_out(const SpanSet *ss);
extern uint8_t *set_as_wkb(const Set *s, uint8_t variant, size_t *size_out);
extern char *set_as_hexwkb(const Set *s, uint8_t variant, size_t *size_out);
extern Set *set_from_hexwkb(const char *hexwkb);
extern Set *set_from_wkb(const uint8_t *wkb, int size);
extern char *set_out(const Set *s, int maxdd);
extern uint8_t *span_as_wkb(const Span *s, uint8_t variant, size_t *size_out);
extern char *span_as_hexwkb(const Span *s, uint8_t variant, size_t *size_out);
extern Span *span_from_hexwkb(const char *hexwkb);
extern Span *span_from_wkb(const uint8_t *wkb, int size);
extern char *span_out(const Span *s, int maxdd);
extern uint8_t *spanset_as_wkb(const SpanSet *ss, uint8_t variant, size_t *size_out);
extern char *spanset_as_hexwkb(const SpanSet *ss, uint8_t variant, size_t *size_out);
extern SpanSet *spanset_from_hexwkb(const char *hexwkb);
extern SpanSet *spanset_from_wkb(const uint8_t *wkb, int size);
extern char *spanset_out(const SpanSet *ss, int maxdd);
extern Set *textset_in(const char *str);
extern char *textset_out(const Set *set);
extern Set *tstzset_in(const char *str);
extern char *tstzset_out(const Set *set);





extern Span *bigintspan_make(int64 lower, int64 upper, bool lower_inc, bool upper_inc);
extern Span *floatspan_make(double lower, double upper, bool lower_inc, bool upper_inc);
extern Span *intspan_make(int lower, int upper, bool lower_inc, bool upper_inc);
extern Set *set_copy(const Set *ts);
extern Span *tstzspan_make(TimestampTz lower, TimestampTz upper, bool lower_inc, bool upper_inc);
extern Span *span_copy(const Span *s);
extern SpanSet *spanset_copy(const SpanSet *ps);
extern SpanSet *spanset_make(Span *spans, int count, bool normalize);
extern SpanSet *spanset_make_exp(Span *spans, int count, int maxcount, bool normalize, bool ordered);
extern SpanSet *spanset_make_free(Span *spans, int count, bool normalize);
extern Set *tstzset_make(const TimestampTz *times, int count);





extern Set *bigint_to_bigintset(int64 i);
extern Span *bigint_to_bigintspan(int i);
extern Span *float_to_floaspan(double d);
extern Set *float_to_floatset(double d);
extern Set *int_to_intset(int i);
extern Span *int_to_intspan(int i);
extern void set_set_span(const Set *os, Span *s);
extern Span *set_to_span(const Set *s);
extern SpanSet *set_to_spanset(const Set *s);
extern SpanSet *span_to_spanset(const Span *s);
extern Span *spanset_to_span(const SpanSet *ss);
extern void spatialset_set_stbox(const Set *set, STBox *box);
extern STBox *spatialset_to_stbox(const Set *s);
extern Span *timestamp_to_period(TimestampTz t);
extern SpanSet *timestamp_to_periodset(TimestampTz t);
extern Set *timestamp_to_tstzset(TimestampTz t);





extern int64 bigintset_end_value(const Set *s);
extern int64 bigintset_start_value(const Set *s);
extern bool bigintset_value_n(const Set *s, int n, int64 *result);
extern int64 *bigintset_values(const Set *s);
extern int bigintspan_lower(const Span *s);
extern int bigintspan_upper(const Span *s);
extern int bigintspanset_lower(const SpanSet *ss);
extern int bigintspanset_upper(const SpanSet *ss);
extern double floatset_end_value(const Set *s);
extern double floatset_start_value(const Set *s);
extern bool floatset_value_n(const Set *s, int n, double *result);
extern double *floatset_values(const Set *s);
extern double floatspan_lower(const Span *s);
extern double floatspan_upper(const Span *s);
extern double floatspanset_lower(const SpanSet *ss);
extern double floatspanset_upper(const SpanSet *ss);
extern int intset_end_value(const Set *s);
extern int intset_start_value(const Set *s);
extern bool intset_value_n(const Set *s, int n, int *result);
extern int *intset_values(const Set *s);
extern int intspan_lower(const Span *s);
extern int intspan_upper(const Span *s);
extern int intspanset_lower(const SpanSet *ss);
extern int intspanset_upper(const SpanSet *ss);
extern Datum set_end_value(const Set *s);
extern uint32 set_hash(const Set *s);
extern uint64 set_hash_extended(const Set *s, uint64 seed);
extern int set_mem_size(const Set *s);
extern int set_num_values(const Set *s);
extern Datum set_start_value(const Set *s);
extern bool set_value_n(const Set *s, int n, Datum *result);
extern Datum *set_values(const Set *s);
extern Interval *period_duration(const Span *s);
extern TimestampTz period_lower(const Span *p);
extern TimestampTz period_upper(const Span *p);
extern Interval *periodset_duration(const SpanSet *ps, bool boundspan);
extern TimestampTz periodset_end_timestamp(const SpanSet *ps);
extern TimestampTz periodset_lower(const SpanSet *ps);
extern int periodset_num_timestamps(const SpanSet *ps);
extern TimestampTz periodset_start_timestamp(const SpanSet *ps);
extern bool periodset_timestamp_n(const SpanSet *ps, int n, TimestampTz *result);
extern TimestampTz *periodset_timestamps(const SpanSet *ps, int *count);
extern TimestampTz periodset_upper(const SpanSet *ps);
extern uint32 span_hash(const Span *s);
extern uint64 span_hash_extended(const Span *s, Datum seed);
extern bool span_lower_inc(const Span *s);
extern bool span_upper_inc(const Span *s);
extern double span_width(const Span *s);
extern Span *spanset_end_span(const SpanSet *ss);
extern uint32 spanset_hash(const SpanSet *ps);
extern uint64 spanset_hash_extended(const SpanSet *ps, uint64 seed);
extern bool spanset_lower_inc(const SpanSet *ss);
extern int spanset_mem_size(const SpanSet *ss);
extern int spanset_num_spans(const SpanSet *ss);
extern Span *spanset_span_n(const SpanSet *ss, int i);
extern const Span **spanset_spans(const SpanSet *ss);
extern Span *spanset_start_span(const SpanSet *ss);
extern bool spanset_upper_inc(const SpanSet *ss);
extern double spanset_width(const SpanSet *ss);
extern TimestampTz tstzset_end_timestamp(const Set *ts);
extern TimestampTz tstzset_start_timestamp(const Set *ts);
extern bool tstzset_timestamp_n(const Set *ts, int n, TimestampTz *result);
extern TimestampTz *tstzset_values(const Set *ts);
extern int geoset_srid(const Set *set);





extern void floatspan_set_intspan(const Span *s1, Span *s2);
extern void intspan_set_floatspan(const Span *s1, Span *s2);
extern void numspan_set_floatspan(const Span *s1, Span *s2);
extern Span *period_tprecision(const Span *s, const Interval *duration, TimestampTz torigin);
extern SpanSet *periodset_tprecision(const SpanSet *ss, const Interval *duration, TimestampTz torigin);
extern void period_shift_tscale(Span *p, const Interval *shift, const Interval *duration,
  TimestampTz *delta, double *scale);
extern SpanSet *periodset_shift_tscale(const SpanSet *ps, const Interval *shift, const Interval *duration);
extern Set *set_shift(const Set *s, Datum shift);
extern void span_expand(const Span *s1, Span *s2);
extern TimestampTz timestamp_tprecision(TimestampTz t, const Interval *duration, TimestampTz torigin);
extern Set *tstzset_shift_tscale(const Set *ts, const Interval *shift, const Interval *duration);

/*****************************************************************************
 * Bounding box functions for set and span types
 *****************************************************************************/



extern bool adjacent_bigintspan_bigint(const Span *s, int64 i);
extern bool adjacent_bigintspanset_bigint(const SpanSet *ss, int64 i);
extern bool adjacent_floatspan_float(const Span *s, double d);
extern bool adjacent_intspan_int(const Span *s, int i);
extern bool adjacent_period_timestamp(const Span *p, TimestampTz t);
extern bool adjacent_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern bool adjacent_span_span(const Span *s1, const Span *s2);
extern bool adjacent_spanset_span(const SpanSet *ss, const Span *s);
extern bool adjacent_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool contained_bigint_bigintset(int64 i, const Set *s);
extern bool contained_bigint_bigintspan(int64 i, const Span *s);
extern bool contained_bigint_bigintspanset(int64 i, const SpanSet *ss);
extern bool contained_float_floatset(double d, const Set *s);
extern bool contained_float_floatspan(double d, const Span *s);
extern bool contained_float_floatspanset(double d, const SpanSet *ss);
extern bool contained_int_intset(int i, const Set *s);
extern bool contained_int_intspanset (int i, const SpanSet *ss);
extern bool contained_int_intspan(int i, const Span *s);
extern bool contained_set_set(const Set *s1, const Set *s2);
extern bool contained_span_span(const Span *s1, const Span *s2);
extern bool contained_span_spanset(const Span *s, const SpanSet *ss);
extern bool contained_spanset_span(const SpanSet *ss, const Span *s);
extern bool contained_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool contained_timestamp_period(TimestampTz t, const Span *p);
extern bool contained_timestamp_timestampset(TimestampTz t, const Set *ts);
extern bool contains_floatspan_float(const Span *s, double d);
extern bool contains_floatspanset_float(const SpanSet *ss, double d);
extern bool contains_intspan_int(const Span *s, int i);
extern bool contains_set_set(const Set *s1, const Set *s2);
extern bool contains_period_timestamp(const Span *p, TimestampTz t);
extern bool contains_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern bool contains_span_span(const Span *s1, const Span *s2);
extern bool contains_span_spanset(const Span *s, const SpanSet *ss);
extern bool contains_spanset_span(const SpanSet *ss, const Span *s);
extern bool contains_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool contains_timestampset_timestamp(const Set *ts, TimestampTz t);
extern bool overlaps_set_set(const Set *s1, const Set *s2);
extern bool overlaps_span_span(const Span *s1, const Span *s2);
extern bool overlaps_spanset_span(const SpanSet *ss, const Span *s);
extern bool overlaps_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);





extern bool after_timestamp_timestampset(TimestampTz t, const Set *ts);
extern bool before_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern bool before_timestamp_timestampset(TimestampTz t, const Set *ts);
extern bool left_float_floatspan(double d, const Span *s);
extern bool left_floatspan_float(const Span *s, double d);
extern bool left_int_intspan(int i, const Span *s);
extern bool left_intspan_int(const Span *s, int i);
extern bool left_set_set(const Set *s1, const Set *s2);
extern bool left_span_span(const Span *s1, const Span *s2);
extern bool left_span_spanset(const Span *s, const SpanSet *ss);
extern bool left_spanset_span(const SpanSet *ss, const Span *s);
extern bool left_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool overafter_period_timestamp(const Span *p, TimestampTz t);
extern bool overafter_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern bool overafter_timestamp_period(TimestampTz t, const Span *p);
extern bool overafter_timestamp_periodset(TimestampTz t, const SpanSet *ps);
extern bool overafter_timestamp_timestampset(TimestampTz t, const Set *ts);
extern bool overbefore_period_timestamp(const Span *p, TimestampTz t);
extern bool overbefore_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern bool overbefore_timestamp_period(TimestampTz t, const Span *p);
extern bool overbefore_timestamp_periodset(TimestampTz t, const SpanSet *ps);
extern bool overbefore_timestamp_timestampset(TimestampTz t, const Set *ts);
extern bool overleft_float_floatspan(double d, const Span *s);
extern bool overleft_floatspan_float(const Span *s, double d);
extern bool overleft_int_intspan(int i, const Span *s);
extern bool overleft_intspan_int(const Span *s, int i);
extern bool overleft_set_set(const Set *s1, const Set *s2);
extern bool overleft_span_span(const Span *s1, const Span *s2);
extern bool overleft_span_spanset(const Span *s, const SpanSet *ss);
extern bool overleft_spanset_span(const SpanSet *ss, const Span *s);
extern bool overleft_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool overright_float_floatspan(double d, const Span *s);
extern bool overright_floatspan_float(const Span *s, double d);
extern bool overright_int_intspan(int i, const Span *s);
extern bool overright_intspan_int(const Span *s, int i);
extern bool overright_set_set(const Set *s1, const Set *s2);
extern bool overright_span_span(const Span *s1, const Span *s2);
extern bool overright_span_spanset(const Span *s, const SpanSet *ss);
extern bool overright_spanset_span(const SpanSet *ss, const Span *s);
extern bool overright_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool right_float_floatspan(double d, const Span *s);
extern bool right_floatspan_float(const Span *s, double d);
extern bool right_int_intspan(int i, const Span *s);
extern bool right_intspan_int(const Span *s, int i);
extern bool right_set_set(const Set *s1, const Set *s2);
extern bool right_span_span(const Span *s1, const Span *s2);
extern bool right_span_spanset(const Span *s, const SpanSet *ss);
extern bool right_spanset_span(const SpanSet *ss, const Span *s);
extern bool right_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);





extern void bbox_union_span_span(const Span *s1, const Span *s2, Span *result);
extern Set *intersection_set_set(const Set *s1, const Set *s2);
extern bool intersection_period_timestamp(const Span *p, TimestampTz t, TimestampTz *result);
extern bool intersection_periodset_timestamp(const SpanSet *ps, TimestampTz t, TimestampTz *result);
extern Span *intersection_span_span(const Span *s1, const Span *s2);
extern SpanSet *intersection_spanset_span(const SpanSet *ss, const Span *s);
extern SpanSet *intersection_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool intersection_timestampset_timestamp(const Set *ts, const TimestampTz t, TimestampTz *result);
extern Set *minus_set_set(const Set *s1, const Set *s2);
extern SpanSet *minus_period_timestamp(const Span *p, TimestampTz t);
extern SpanSet *minus_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern SpanSet *minus_span_span(const Span *s1, const Span *s2);
extern SpanSet *minus_span_spanset(const Span *s, const SpanSet *ss);
extern SpanSet *minus_spanset_span(const SpanSet *ss, const Span *s);
extern SpanSet *minus_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern bool minus_timestamp_period(TimestampTz t, const Span *p, TimestampTz *result);
extern bool minus_timestamp_periodset(TimestampTz t, const SpanSet *ps, TimestampTz *result);
extern Set *minus_timestampset_timestamp(const Set *ts, TimestampTz t);
extern Set *union_set_set(const Set *s1, const Set *s2);
extern SpanSet *union_period_timestamp(const Span *p, TimestampTz t);
extern SpanSet *union_periodset_timestamp(SpanSet *ps, TimestampTz t);
extern SpanSet *union_span_span(const Span *s1, const Span *s2);
extern SpanSet *union_spanset_span(const SpanSet *ss, const Span *s);
extern SpanSet *union_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern Set *union_timestamp_timestampset(TimestampTz t, const Set *ts);
extern Set *union_timestampset_timestamp(const Set *ts, const TimestampTz t);





extern double distance_floatspan_float(const Span *s, double d);
extern double distance_intspan_int(const Span *s, int i);
extern double distance_set_set(const Set *s1, const Set *s2);
extern double distance_period_timestamp(const Span *p, TimestampTz t);
extern double distance_periodset_timestamp(const SpanSet *ps, TimestampTz t);
extern double distance_span_span(const Span *s1, const Span *s2);
extern double distance_spanset_span(const SpanSet *ss, const Span *s);
extern double distance_spanset_spanset(const SpanSet *ss1, const SpanSet *ss2);
extern double distance_timestampset_timestamp(const Set *ts, TimestampTz t);





extern Span *bigint_extent_transfn(Span *s, int64 i);
extern Set *bigint_union_transfn(Set *state, int64 i);
extern Span *int_extent_transfn(Span *s, int i);
extern Set *int_union_transfn(Set *state, int i);
extern Span *float_extent_transfn(Span *s, double d);
extern Set *float_union_transfn(Set *state, double d);
extern SkipList *period_tcount_transfn(SkipList *state, const Span *p);
extern SkipList *periodset_tcount_transfn(SkipList *state, const SpanSet *ps);
extern Set *set_union_finalfn(Set *state);
extern Set *set_union_transfn(Set *state, Set *set);
extern Span *span_extent_transfn(Span *s1, const Span *s2);
extern Span *spanset_extent_transfn(Span *s, const SpanSet *ss);
extern Set *text_union_transfn(Set *state, const text *txt);
extern Span *timestamp_extent_transfn(Span *p, TimestampTz t);
extern SkipList *timestamp_tcount_transfn(SkipList *state, TimestampTz t);
extern Set *timestamp_union_transfn(Set *state, TimestampTz t);
extern Span *set_extent_transfn(Span *span, const Set *set);
extern SkipList *tstzset_tcount_transfn(SkipList *state, const Set *ts);





extern int set_cmp(const Set *s1, const Set *s2);
extern bool set_eq(const Set *s1, const Set *s2);
extern bool set_ge(const Set *s1, const Set *s2);
extern bool set_gt(const Set *s1, const Set *s2);
extern bool set_le(const Set *s1, const Set *s2);
extern bool set_lt(const Set *s1, const Set *s2);
extern bool set_ne(const Set *s1, const Set *s2);
extern int span_cmp(const Span *s1, const Span *s2);
extern bool span_eq(const Span *s1, const Span *s2);
extern bool span_ge(const Span *s1, const Span *s2);
extern bool span_gt(const Span *s1, const Span *s2);
extern bool span_le(const Span *s1, const Span *s2);
extern bool span_lt(const Span *s1, const Span *s2);
extern bool span_ne(const Span *s1, const Span *s2);
extern int spanset_cmp(const SpanSet *ss1, const SpanSet *ss2);
extern bool spanset_eq(const SpanSet *ss1, const SpanSet *ss2);
extern bool spanset_ge(const SpanSet *ss1, const SpanSet *ss2);
extern bool spanset_gt(const SpanSet *ss1, const SpanSet *ss2);
extern bool spanset_le(const SpanSet *ss1, const SpanSet *ss2);
extern bool spanset_lt(const SpanSet *ss1, const SpanSet *ss2);
extern bool spanset_ne(const SpanSet *ss1, const SpanSet *ss2);

/******************************************************************************
 * Functions for box types
 *****************************************************************************/



extern TBox *tbox_in(const char *str);
extern char *tbox_out(const TBox *box, int maxdd);
extern TBox *tbox_from_wkb(const uint8_t *wkb, int size);
extern TBox *tbox_from_hexwkb(const char *hexwkb);
extern STBox *stbox_from_wkb(const uint8_t *wkb, int size);
extern STBox *stbox_from_hexwkb(const char *hexwkb);
extern uint8_t *tbox_as_wkb(const TBox *box, uint8_t variant, size_t *size_out);
extern char *tbox_as_hexwkb(const TBox *box, uint8_t variant, size_t *size);
extern uint8_t *stbox_as_wkb(const STBox *box, uint8_t variant, size_t *size_out);
extern char *stbox_as_hexwkb(const STBox *box, uint8_t variant, size_t *size);
extern STBox *stbox_in(const char *str);
extern char *stbox_out(const STBox *box, int maxdd);





extern TBox *tbox_make(const Span *p, const Span *s);
extern void tbox_set(const Span *p, const Span *s, TBox *box);
extern TBox *tbox_copy(const TBox *box);
extern STBox * stbox_make(bool hasx, bool hasz, bool geodetic, int32 srid,
  double xmin, double xmax, double ymin, double ymax, double zmin, double zmax, const Span *p);
extern void stbox_set(bool hasx, bool hasz, bool geodetic, int32 srid, double xmin, double xmax,
  double ymin, double ymax, double zmin, double zmax, const Span *p, STBox *box);
extern STBox *stbox_copy(const STBox *box);





extern TBox *int_to_tbox(int i);
extern TBox *float_to_tbox(double d);
extern TBox *timestamp_to_tbox(TimestampTz t);
extern TBox *tstzset_to_tbox(const Set *ss);
extern TBox *period_to_tbox(const Span *p);
extern TBox *periodset_to_tbox(const SpanSet *ps);
extern TBox *int_timestamp_to_tbox(int i, TimestampTz t);
extern TBox *float_period_to_tbox(double d, const Span *p);
extern TBox *float_timestamp_to_tbox(double d, TimestampTz t);
extern STBox *geo_period_to_stbox(const GSERIALIZED *gs, const Span *p);
extern STBox *geo_timestamp_to_stbox(const GSERIALIZED *gs, TimestampTz t);
extern TBox *int_period_to_tbox(int i, const Span *p);
extern TBox *numspan_to_tbox(const Span *s);
extern TBox *span_timestamp_to_tbox(const Span *span, TimestampTz t);
extern TBox *span_period_to_tbox(const Span *span, const Span *p);
extern Span *tbox_to_floatspan(const TBox *box);
extern Span *tbox_to_period(const TBox *box);
extern Span *stbox_to_period(const STBox *box);
extern TBox *tnumber_to_tbox(const Temporal *temp);
extern GSERIALIZED *stbox_to_geo(const STBox *box);
extern STBox *tpoint_to_stbox(const Temporal *temp);
extern STBox *geo_to_stbox(const GSERIALIZED *gs);
extern STBox *timestamp_to_stbox(TimestampTz t);
extern STBox *tstzset_to_stbox(const Set *ts);
extern STBox *period_to_stbox(const Span *p);
extern STBox *periodset_to_stbox(const SpanSet *ps);





extern bool tbox_hasx(const TBox *box);
extern bool tbox_hast(const TBox *box);
extern bool tbox_xmin(const TBox *box, double *result);
extern bool tbox_xmax(const TBox *box, double *result);
extern bool tbox_tmin(const TBox *box, TimestampTz *result);
extern bool tbox_tmax(const TBox *box, TimestampTz *result);
extern bool stbox_hasx(const STBox *box);
extern bool stbox_hasz(const STBox *box);
extern bool stbox_hast(const STBox *box);
extern bool stbox_isgeodetic(const STBox *box);
extern bool stbox_xmin(const STBox *box, double *result);
extern bool stbox_xmax(const STBox *box, double *result);
extern bool stbox_ymin(const STBox *box, double *result);
extern bool stbox_ymax(const STBox *box, double *result);
extern bool stbox_zmin(const STBox *box, double *result);
extern bool stbox_zmax(const STBox *box, double *result);
extern bool stbox_tmin(const STBox *box, TimestampTz *result);
extern bool stbox_tmax(const STBox *box, TimestampTz *result);
extern int32 stbox_srid(const STBox *box);





extern void tbox_expand(const TBox *box1, TBox *box2);
extern TBox *tbox_expand_value(const TBox *box, const double d);
extern TBox *tbox_expand_time(const TBox *box, const Interval *interval);
extern void stbox_expand(const STBox *box1, STBox *box2);
extern STBox *stbox_set_srid(const STBox *box, int32 srid);
extern STBox *stbox_expand_space(const STBox *box, double d);
extern STBox *stbox_expand_time(const STBox *box, const Interval *interval);





extern bool contains_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool contained_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool overlaps_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool same_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool adjacent_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool contains_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool contained_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overlaps_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool same_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool adjacent_stbox_stbox(const STBox *box1, const STBox *box2);





extern bool left_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool overleft_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool right_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool overright_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool before_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool overbefore_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool after_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool overafter_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool left_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overleft_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool right_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overright_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool below_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overbelow_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool above_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overabove_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool front_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overfront_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool back_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overback_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool before_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overbefore_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool after_stbox_stbox(const STBox *box1, const STBox *box2);
extern bool overafter_stbox_stbox(const STBox *box1, const STBox *box2);





extern TBox *union_tbox_tbox(const TBox *box1, const TBox *box2);
extern bool inter_tbox_tbox(const TBox *box1, const TBox *box2, TBox *result);
extern TBox *intersection_tbox_tbox(const TBox *box1, const TBox *box2);
extern STBox *union_stbox_stbox(const STBox *box1, const STBox *box2, bool strict);
extern bool inter_stbox_stbox(const STBox *box1, const STBox *box2, STBox *result);
extern STBox *intersection_stbox_stbox(const STBox *box1, const STBox *box2);





extern bool tbox_eq(const TBox *box1, const TBox *box2);
extern bool tbox_ne(const TBox *box1, const TBox *box2);
extern int tbox_cmp(const TBox *box1, const TBox *box2);
extern bool tbox_lt(const TBox *box1, const TBox *box2);
extern bool tbox_le(const TBox *box1, const TBox *box2);
extern bool tbox_ge(const TBox *box1, const TBox *box2);
extern bool tbox_gt(const TBox *box1, const TBox *box2);
extern bool stbox_eq(const STBox *box1, const STBox *box2);
extern bool stbox_ne(const STBox *box1, const STBox *box2);
extern int stbox_cmp(const STBox *box1, const STBox *box2);
extern bool stbox_lt(const STBox *box1, const STBox *box2);
extern bool stbox_le(const STBox *box1, const STBox *box2);
extern bool stbox_ge(const STBox *box1, const STBox *box2);
extern bool stbox_gt(const STBox *box1, const STBox *box2);

/*****************************************************************************
 * Functions for temporal types
 *****************************************************************************/



extern text *cstring2text(const char *cstring);
extern char *text2cstring(const text *textptr);



extern Temporal *tbool_in(const char *str);
extern char *tbool_out(const Temporal *temp);
extern char *temporal_as_hexwkb(const Temporal *temp, uint8_t variant, size_t *size_out);
extern char *temporal_as_mfjson(const Temporal *temp, bool with_bbox, int flags, int precision, char *srs);
extern uint8_t *temporal_as_wkb(const Temporal *temp, uint8_t variant, size_t *size_out);
extern Temporal *temporal_from_hexwkb(const char *hexwkb);
extern Temporal *temporal_from_mfjson(const char *mfjson);
extern Temporal *temporal_from_wkb(const uint8_t *wkb, int size);
extern Temporal *tfloat_in(const char *str);
extern char *tfloat_out(const Temporal *temp, int maxdd);
extern Temporal *tgeogpoint_in(const char *str);
extern Temporal *tgeompoint_in(const char *str);
extern Temporal *tint_in(const char *str);
extern char *tint_out(const Temporal *temp);
extern char *tpoint_as_ewkt(const Temporal *temp, int maxdd);
extern char *tpoint_as_text(const Temporal *temp, int maxdd);
extern char *tpoint_out(const Temporal *temp, int maxdd);
extern Temporal *ttext_in(const char *str);
extern char *ttext_out(const Temporal *temp);





extern Temporal *tbool_from_base(bool b, const Temporal *temp);
extern TInstant *tboolinst_make(bool b, TimestampTz t);
extern TSequence *tbooldiscseq_from_base_time(bool b, const Set *ts);
extern TSequence *tboolseq_from_base(bool b, const TSequence *seq);
extern TSequence *tboolseq_from_base_time(bool b, const Span *p);
extern TSequenceSet *tboolseqset_from_base(bool b, const TSequenceSet *ss);
extern TSequenceSet *tboolseqset_from_base_time(bool b, const SpanSet *ps);
extern Temporal *temporal_copy(const Temporal *temp);
extern Temporal *tfloat_from_base(double d, const Temporal *temp, interpType interp);
extern TInstant *tfloatinst_make(double d, TimestampTz t);
extern TSequence *tfloatdiscseq_from_base_time(double d, const Set *ts);
extern TSequence *tfloatseq_from_base(double d, const TSequence *seq, interpType interp);
extern TSequence *tfloatseq_from_base_time(double d, const Span *p, interpType interp);
extern TSequenceSet *tfloatseqset_from_base(double d, const TSequenceSet *ss, interpType interp);
extern TSequenceSet *tfloatseqset_from_base_time(double d, const SpanSet *ps, interpType interp);
extern Temporal *tgeogpoint_from_base(const GSERIALIZED *gs, const Temporal *temp, interpType interp);
extern TInstant *tgeogpointinst_make(const GSERIALIZED *gs, TimestampTz t);
extern TSequence *tgeogpointdiscseq_from_base_time(const GSERIALIZED *gs, const Set *ts);
extern TSequence *tgeogpointseq_from_base(const GSERIALIZED *gs, const TSequence *seq, interpType interp);
extern TSequence *tgeogpointseq_from_base_time(const GSERIALIZED *gs, const Span *p, interpType interp);
extern TSequenceSet *tgeogpointseqset_from_base(const GSERIALIZED *gs, const TSequenceSet *ss, interpType interp);
extern TSequenceSet *tgeogpointseqset_from_base_time(const GSERIALIZED *gs, const SpanSet *ps, interpType interp);
extern Temporal *tgeompoint_from_base(const GSERIALIZED *gs, const Temporal *temp, interpType interp);
extern TInstant *tgeompointinst_make(const GSERIALIZED *gs, TimestampTz t);
extern TSequence *tgeompointdiscseq_from_base_time(const GSERIALIZED *gs, const Set *ts);
extern TSequence *tgeompointseq_from_base(const GSERIALIZED *gs, const TSequence *seq, interpType interp);
extern TSequence *tgeompointseq_from_base_time(const GSERIALIZED *gs, const Span *p, interpType interp);
extern TSequenceSet *tgeompointseqset_from_base(const GSERIALIZED *gs, const TSequenceSet *ss, interpType interp);
extern TSequenceSet *tgeompointseqset_from_base_time(const GSERIALIZED *gs, const SpanSet *ps, interpType interp);
extern Temporal *tint_from_base(int i, const Temporal *temp);
extern TInstant *tintinst_make(int i, TimestampTz t);
extern TSequence *tintdiscseq_from_base_time(int i, const Set *ts);
extern TSequence *tintseq_from_base(int i, const TSequence *seq);
extern TSequence *tintseq_from_base_time(int i, const Span *p);
extern TSequenceSet *tintseqset_from_base(int i, const TSequenceSet *ss);
extern TSequenceSet *tintseqset_from_base_time(int i, const SpanSet *ps);
extern TSequence *tsequence_make(const TInstant **instants, int count, bool lower_inc, bool upper_inc, interpType interp, bool normalize);
extern TSequence *tsequence_make_exp(const TInstant **instants, int count, int maxcount, bool lower_inc, bool upper_inc, interpType interp, bool normalize);
extern TSequence *tpointseq_make_coords(const double *xcoords, const double *ycoords, const double *zcoords,
  const TimestampTz *times, int count, int32 srid, bool geodetic, bool lower_inc, bool upper_inc, interpType interp, bool normalize);
extern TSequence *tsequence_make_free(TInstant **instants, int count, bool lower_inc, bool upper_inc, interpType interp, bool normalize);
extern TSequenceSet *tsequenceset_make(const TSequence **sequences, int count, bool normalize);
extern TSequenceSet *tsequenceset_make_exp(const TSequence **sequences, int count, int maxcount, bool normalize);
extern TSequenceSet *tsequenceset_make_free(TSequence **sequences, int count, bool normalize);
extern TSequenceSet *tsequenceset_make_gaps(const TInstant **instants, int count, interpType interp, Interval *maxt, double maxdist);
extern Temporal *ttext_from_base(const text *txt, const Temporal *temp);
extern TInstant *ttextinst_make(const text *txt, TimestampTz t);
extern TSequence *ttextdiscseq_from_base_time(const text *txt, const Set *ts);
extern TSequence *ttextseq_from_base(const text *txt, const TSequence *seq);
extern TSequence *ttextseq_from_base_time(const text *txt, const Span *p);
extern TSequenceSet *ttextseqset_from_base(const text *txt, const TSequenceSet *ss);
extern TSequenceSet *ttextseqset_from_base_time(const text *txt, const SpanSet *ps);





extern Temporal *tfloat_to_tint(const Temporal *temp);
extern Temporal *tint_to_tfloat(const Temporal *temp);
extern Span *tnumber_to_span(const Temporal *temp);
extern Span *temporal_to_period(const Temporal *temp);





extern bool tbool_end_value(const Temporal *temp);
extern bool tbool_start_value(const Temporal *temp);
extern bool *tbool_values(const Temporal *temp, int *count);
extern Interval *temporal_duration(const Temporal *temp, bool boundspan);
extern const TInstant *temporal_end_instant(const Temporal *temp);
extern TSequence *temporal_end_sequence(const Temporal *temp);
extern TimestampTz temporal_end_timestamp(const Temporal *temp);
extern uint32 temporal_hash(const Temporal *temp);
extern const TInstant *temporal_instant_n(const Temporal *temp, int n);
extern const TInstant **temporal_instants(const Temporal *temp, int *count);
extern char *temporal_interpolation(const Temporal *temp);
extern const TInstant *temporal_max_instant(const Temporal *temp);
extern const TInstant *temporal_min_instant(const Temporal *temp);
extern int temporal_num_instants(const Temporal *temp);
extern int temporal_num_sequences(const Temporal *temp);
extern int temporal_num_timestamps(const Temporal *temp);
extern TSequence **temporal_segments(const Temporal *temp, int *count);
extern TSequence *temporal_sequence_n(const Temporal *temp, int i);
extern TSequence **temporal_sequences(const Temporal *temp, int *count);
extern const TInstant *temporal_start_instant(const Temporal *temp);
extern TSequence *temporal_start_sequence(const Temporal *temp);
extern TimestampTz temporal_start_timestamp(const Temporal *temp);
extern char *temporal_subtype(const Temporal *temp);
extern SpanSet *temporal_time(const Temporal *temp);
extern bool temporal_timestamp_n(const Temporal *temp, int n, TimestampTz *result);
extern TimestampTz *temporal_timestamps(const Temporal *temp, int *count);
extern double tfloat_end_value(const Temporal *temp);
extern double tfloat_max_value(const Temporal *temp);
extern double tfloat_min_value(const Temporal *temp);
extern double tfloat_start_value(const Temporal *temp);
extern double *tfloat_values(const Temporal *temp, int *count);
extern int tint_end_value(const Temporal *temp);
extern int tint_max_value(const Temporal *temp);
extern int tint_min_value(const Temporal *temp);
extern int tint_start_value(const Temporal *temp);
extern int *tint_values(const Temporal *temp, int *count);
extern SpanSet *tnumber_values(const Temporal *temp);
extern GSERIALIZED *tpoint_end_value(const Temporal *temp);
extern GSERIALIZED *tpoint_start_value(const Temporal *temp);
extern GSERIALIZED **tpoint_values(const Temporal *temp, int *count);
extern text *ttext_end_value(const Temporal *temp);
extern text *ttext_max_value(const Temporal *temp);
extern text *ttext_min_value(const Temporal *temp);
extern text *ttext_start_value(const Temporal *temp);
extern text **ttext_values(const Temporal *temp, int *count);





extern Temporal *temporal_append_tinstant(Temporal *temp, const TInstant *inst, double maxdist, Interval *maxt, bool expand);
extern Temporal *temporal_append_tsequence(Temporal *temp, const TSequence *seq, bool expand);
extern Temporal *temporal_merge(const Temporal *temp1, const Temporal *temp2);
extern Temporal *temporal_merge_array(Temporal **temparr, int count);
extern Temporal *temporal_shift(const Temporal *temp, const Interval *shift);
extern Temporal *temporal_shift_tscale(const Temporal *temp, const Interval *shift, const Interval *duration);
extern Temporal *temporal_step_to_linear(const Temporal *temp);
extern Temporal *temporal_to_tinstant(const Temporal *temp);
extern Temporal *temporal_to_tdiscseq(const Temporal *temp);
extern Temporal *temporal_to_tcontseq(const Temporal *temp);
extern Temporal *temporal_to_tsequenceset(const Temporal *temp);
extern Temporal *temporal_tscale(const Temporal *temp, const Interval *duration);
extern Temporal *temporal_tprecision(const Temporal *temp, const Interval *duration, TimestampTz origin);
extern Temporal *temporal_tsample(const Temporal *temp, const Interval *duration, TimestampTz origin);





extern Temporal *tbool_at_value(const Temporal *temp, bool b);
extern Temporal *tbool_minus_value(const Temporal *temp, bool b);
extern bool tbool_value_at_timestamp(const Temporal *temp, TimestampTz t, bool strict, bool *value);
extern Temporal *temporal_at_max(const Temporal *temp);
extern Temporal *temporal_at_min(const Temporal *temp);
extern Temporal *temporal_at_period(const Temporal *temp, const Span *p);
extern Temporal *temporal_at_periodset(const Temporal *temp, const SpanSet *ps);
extern Temporal *temporal_at_timestamp(const Temporal *temp, TimestampTz t);
extern Temporal *temporal_at_timestampset(const Temporal *temp, const Set *ts);
extern Temporal *temporal_minus_max(const Temporal *temp);
extern Temporal *temporal_minus_min(const Temporal *temp);
extern Temporal *temporal_minus_period(const Temporal *temp, const Span *p);
extern Temporal *temporal_minus_periodset(const Temporal *temp, const SpanSet *ps);
extern Temporal *temporal_minus_timestamp(const Temporal *temp, TimestampTz t);
extern Temporal *temporal_minus_timestampset(const Temporal *temp, const Set *ts);
extern Temporal *tfloat_at_value(const Temporal *temp, double d);
extern Temporal *tfloat_minus_value(const Temporal *temp, double d);
extern bool tfloat_value_at_timestamp(const Temporal *temp, TimestampTz t, bool strict, double *value);
extern Temporal *tint_at_value(const Temporal *temp, int i);
extern Temporal *tint_minus_value(const Temporal *temp, int i);
extern bool tint_value_at_timestamp(const Temporal *temp, TimestampTz t, bool strict, int *value);
extern Temporal *tnumber_at_span(const Temporal *temp, const Span *span);
extern Temporal *tnumber_at_spanset(const Temporal *temp, const SpanSet *ss);
extern Temporal *tnumber_at_tbox(const Temporal *temp, const TBox *box);
extern Temporal *tnumber_minus_span(const Temporal *temp, const Span *span);
extern Temporal *tnumber_minus_spanset(const Temporal *temp, const SpanSet *ss);
extern Temporal *tnumber_minus_tbox(const Temporal *temp, const TBox *box);
extern Temporal *tpoint_at_geometry(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *tpoint_at_stbox(const Temporal *temp, const STBox *box);
extern Temporal *tpoint_at_value(const Temporal *temp, GSERIALIZED *gs);
extern Temporal *tpoint_minus_geometry(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *tpoint_minus_stbox(const Temporal *temp, const STBox *box);
extern Temporal *tpoint_minus_value(const Temporal *temp, GSERIALIZED *gs);
extern bool tpoint_value_at_timestamp(const Temporal *temp, TimestampTz t, bool strict, GSERIALIZED **value);
extern TSequence *tsequence_at_period(const TSequence *seq, const Span *p);
extern Temporal *ttext_at_value(const Temporal *temp, text *txt);
extern Temporal *ttext_minus_value(const Temporal *temp, text *txt);
extern bool ttext_value_at_timestamp(const Temporal *temp, TimestampTz t, bool strict, text **value);





extern Temporal *tand_bool_tbool(bool b, const Temporal *temp);
extern Temporal *tand_tbool_bool(const Temporal *temp, bool b);
extern Temporal *tand_tbool_tbool(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tnot_tbool(const Temporal *temp);
extern Temporal *tor_bool_tbool(bool b, const Temporal *temp);
extern Temporal *tor_tbool_bool(const Temporal *temp, bool b);
extern Temporal *tor_tbool_tbool(const Temporal *temp1, const Temporal *temp2);
extern SpanSet *tbool_when_true(const Temporal *temp);





extern Temporal *add_float_tfloat(double d, const Temporal *tnumber);
extern Temporal *add_int_tint(int i, const Temporal *tnumber);
extern Temporal *add_tfloat_float(const Temporal *tnumber, double d);
extern Temporal *add_tint_int(const Temporal *tnumber, int i);
extern Temporal *add_tnumber_tnumber(const Temporal *tnumber1, const Temporal *tnumber2);
extern double float_degrees(double value, bool normalize);
extern Temporal *div_float_tfloat(double d, const Temporal *tnumber);
extern Temporal *div_int_tint(int i, const Temporal *tnumber);
extern Temporal *div_tfloat_float(const Temporal *tnumber, double d);
extern Temporal *div_tint_int(const Temporal *tnumber, int i);
extern Temporal *div_tnumber_tnumber(const Temporal *tnumber1, const Temporal *tnumber2);
extern Temporal *mult_float_tfloat(double d, const Temporal *tnumber);
extern Temporal *mult_int_tint(int i, const Temporal *tnumber);
extern Temporal *mult_tfloat_float(const Temporal *tnumber, double d);
extern Temporal *mult_tint_int(const Temporal *tnumber, int i);
extern Temporal *mult_tnumber_tnumber(const Temporal *tnumber1, const Temporal *tnumber2);
extern Temporal *sub_float_tfloat(double d, const Temporal *tnumber);
extern Temporal *sub_int_tint(int i, const Temporal *tnumber);
extern Temporal *sub_tfloat_float(const Temporal *tnumber, double d);
extern Temporal *sub_tint_int(const Temporal *tnumber, int i);
extern Temporal *sub_tnumber_tnumber(const Temporal *tnumber1, const Temporal *tnumber2);
extern Temporal *tfloat_degrees(const Temporal *temp, bool normalize);
extern Temporal *tfloat_radians(const Temporal *temp);
extern Temporal *tfloat_derivative(const Temporal *temp);
extern Temporal *tnumber_abs(const Temporal *temp);
extern Temporal *tnumber_delta_value(const Temporal *temp);





extern Temporal *textcat_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *textcat_ttext_text(const Temporal *temp, const text *txt);
extern Temporal *textcat_ttext_ttext(const Temporal *temp1, const Temporal *temp2);
extern Temporal *ttext_upper(const Temporal *temp);
extern Temporal *ttext_lower(const Temporal *temp);

/*****************************************************************************
 * Bounding box functions for temporal types
 *****************************************************************************/











extern Temporal *distance_tfloat_float(const Temporal *temp, double d);
extern Temporal *distance_tint_int(const Temporal *temp, int i);
extern Temporal *distance_tnumber_tnumber(const Temporal *temp1, const Temporal *temp2);
extern Temporal *distance_tpoint_geo(const Temporal *temp, const GSERIALIZED *geo);
extern Temporal *distance_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2);
extern double nad_stbox_geo(const STBox *box, const GSERIALIZED *gs);
extern double nad_stbox_stbox(const STBox *box1, const STBox *box2);
extern double nad_tbox_tbox(const TBox *box1, const TBox *box2);
extern double nad_tfloat_float(const Temporal *temp, double d);
extern double nad_tfloat_tfloat(const Temporal *temp1, const Temporal *temp2);
extern int nad_tint_int(const Temporal *temp, int i);
extern int nad_tint_tint(const Temporal *temp1, const Temporal *temp2);
extern double nad_tnumber_tbox(const Temporal *temp, const TBox *box);
extern double nad_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs);
extern double nad_tpoint_stbox(const Temporal *temp, const STBox *box);
extern double nad_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2);
extern TInstant *nai_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs);
extern TInstant *nai_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2);
extern bool shortestline_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs, GSERIALIZED **result);
extern bool shortestline_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2, GSERIALIZED **result);





extern bool tbool_always_eq(const Temporal *temp, bool b);
extern bool tbool_ever_eq(const Temporal *temp, bool b);
extern bool tfloat_always_eq(const Temporal *temp, double d);
extern bool tfloat_always_le(const Temporal *temp, double d);
extern bool tfloat_always_lt(const Temporal *temp, double d);
extern bool tfloat_ever_eq(const Temporal *temp, double d);
extern bool tfloat_ever_le(const Temporal *temp, double d);
extern bool tfloat_ever_lt(const Temporal *temp, double d);
extern bool tgeogpoint_always_eq(const Temporal *temp, GSERIALIZED *gs);;
extern bool tgeogpoint_ever_eq(const Temporal *temp, GSERIALIZED *gs);;
extern bool tgeompoint_always_eq(const Temporal *temp, GSERIALIZED *gs);
extern bool tgeompoint_ever_eq(const Temporal *temp, GSERIALIZED *gs);;
extern bool tint_always_eq(const Temporal *temp, int i);
extern bool tint_always_le(const Temporal *temp, int i);
extern bool tint_always_lt(const Temporal *temp, int i);
extern bool tint_ever_eq(const Temporal *temp, int i);
extern bool tint_ever_le(const Temporal *temp, int i);
extern bool tint_ever_lt(const Temporal *temp, int i);
extern bool ttext_always_eq(const Temporal *temp, text *txt);
extern bool ttext_always_le(const Temporal *temp, text *txt);
extern bool ttext_always_lt(const Temporal *temp, text *txt);
extern bool ttext_ever_eq(const Temporal *temp, text *txt);
extern bool ttext_ever_le(const Temporal *temp, text *txt);
extern bool ttext_ever_lt(const Temporal *temp, text *txt);





extern int temporal_cmp(const Temporal *temp1, const Temporal *temp2);
extern bool temporal_eq(const Temporal *temp1, const Temporal *temp2);
extern bool temporal_ge(const Temporal *temp1, const Temporal *temp2);
extern bool temporal_gt(const Temporal *temp1, const Temporal *temp2);
extern bool temporal_le(const Temporal *temp1, const Temporal *temp2);
extern bool temporal_lt(const Temporal *temp1, const Temporal *temp2);
extern bool temporal_ne(const Temporal *temp1, const Temporal *temp2);
extern Temporal *teq_bool_tbool(bool b, const Temporal *temp);
extern Temporal *teq_float_tfloat(double d, const Temporal *temp);
extern Temporal *teq_geo_tpoint(const GSERIALIZED *geo, const Temporal *tpoint);
extern Temporal *teq_int_tint(int i, const Temporal *temp);
extern Temporal *teq_point_tgeogpoint(const GSERIALIZED *gs, const Temporal *temp);
extern Temporal *teq_point_tgeompoint(const GSERIALIZED *gs, const Temporal *temp);
extern Temporal *teq_tbool_bool(const Temporal *temp, bool b);
extern Temporal *teq_temporal_temporal(const Temporal *temp1, const Temporal *temp2);
extern Temporal *teq_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *teq_tfloat_float(const Temporal *temp, double d);
extern Temporal *teq_tgeogpoint_point(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *teq_tgeompoint_point(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *teq_tint_int(const Temporal *temp, int i);
extern Temporal *teq_tpoint_geo(const Temporal *tpoint, const GSERIALIZED *geo);
extern Temporal *teq_ttext_text(const Temporal *temp, const text *txt);
extern Temporal *tge_float_tfloat(double d, const Temporal *temp);
extern Temporal *tge_int_tint(int i, const Temporal *temp);
extern Temporal *tge_temporal_temporal(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tge_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *tge_tfloat_float(const Temporal *temp, double d);
extern Temporal *tge_tint_int(const Temporal *temp, int i);
extern Temporal *tge_ttext_text(const Temporal *temp, const text *txt);
extern Temporal *tgt_float_tfloat(double d, const Temporal *temp);
extern Temporal *tgt_int_tint(int i, const Temporal *temp);
extern Temporal *tgt_temporal_temporal(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tgt_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *tgt_tfloat_float(const Temporal *temp, double d);
extern Temporal *tgt_tint_int(const Temporal *temp, int i);
extern Temporal *tgt_ttext_text(const Temporal *temp, const text *txt);
extern Temporal *tle_float_tfloat(double d, const Temporal *temp);
extern Temporal *tle_int_tint(int i, const Temporal *temp);
extern Temporal *tle_temporal_temporal(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tle_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *tle_tfloat_float(const Temporal *temp, double d);
extern Temporal *tle_tint_int(const Temporal *temp, int i);
extern Temporal *tle_ttext_text(const Temporal *temp, const text *txt);
extern Temporal *tlt_float_tfloat(double d, const Temporal *temp);
extern Temporal *tlt_int_tint(int i, const Temporal *temp);
extern Temporal *tlt_temporal_temporal(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tlt_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *tlt_tfloat_float(const Temporal *temp, double d);
extern Temporal *tlt_tint_int(const Temporal *temp, int i);
extern Temporal *tlt_ttext_text(const Temporal *temp, const text *txt);
extern Temporal *tne_bool_tbool(bool b, const Temporal *temp);
extern Temporal *tne_float_tfloat(double d, const Temporal *temp);
extern Temporal *tne_geo_tpoint(const GSERIALIZED *geo, const Temporal *tpoint);
extern Temporal *tne_int_tint(int i, const Temporal *temp);
extern Temporal *tne_point_tgeogpoint(const GSERIALIZED *gs, const Temporal *temp);
extern Temporal *tne_point_tgeompoint(const GSERIALIZED *gs, const Temporal *temp);
extern Temporal *tne_tbool_bool(const Temporal *temp, bool b);
extern Temporal *tne_temporal_temporal(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tne_text_ttext(const text *txt, const Temporal *temp);
extern Temporal *tne_tfloat_float(const Temporal *temp, double d);
extern Temporal *tne_tgeogpoint_point(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *tne_tgeompoint_point(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *tne_tint_int(const Temporal *temp, int i);
extern Temporal *tne_tpoint_geo(const Temporal *tpoint, const GSERIALIZED *geo);
extern Temporal *tne_ttext_text(const Temporal *temp, const text *txt);

/*****************************************************************************
  Spatial functions for temporal point types
 *****************************************************************************/



extern bool bearing_point_point(const GSERIALIZED *geo1, const GSERIALIZED *geo2, double *result);
extern Temporal *bearing_tpoint_point(const Temporal *temp, const GSERIALIZED *gs, bool invert);
extern Temporal *bearing_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2);
extern Temporal *tpoint_azimuth(const Temporal *temp);
extern GSERIALIZED *tpoint_convex_hull(const Temporal *temp);
extern Temporal *tpoint_cumulative_length(const Temporal *temp);
extern bool tpoint_direction(const Temporal *temp, double *result);
extern Temporal *tpoint_get_coord(const Temporal *temp, int coord);
extern bool tpoint_is_simple(const Temporal *temp);
extern double tpoint_length(const Temporal *temp);
extern Temporal *tpoint_speed(const Temporal *temp);
extern int tpoint_srid(const Temporal *temp);
extern STBox *tpoint_stboxes(const Temporal *temp, int *count);
extern GSERIALIZED *tpoint_trajectory(const Temporal *temp);





extern STBox *geo_expand_space(const GSERIALIZED *gs, double d);
extern Temporal *tgeompoint_tgeogpoint(const Temporal *temp, bool oper);
extern STBox *tpoint_expand_space(const Temporal *temp, double d);
extern Temporal **tpoint_make_simple(const Temporal *temp, int *count);
extern Temporal *tpoint_set_srid(const Temporal *temp, int32 srid);





extern int econtains_geo_tpoint(const GSERIALIZED *geo, const Temporal *temp);
extern int edisjoint_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs);
extern int edisjoint_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2);
extern int edwithin_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs, double dist);
extern int edwithin_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2, double dist);
extern int eintersects_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs);
extern int eintersects_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2);
extern int etouches_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs);
extern Temporal *tcontains_geo_tpoint(const GSERIALIZED *gs, const Temporal *temp, bool restr, bool atvalue);
extern Temporal *tdisjoint_tpoint_geo(const Temporal *temp, const GSERIALIZED *geo, bool restr, bool atvalue);
extern Temporal *tdwithin_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs, double dist, bool restr, bool atvalue);
extern Temporal *tdwithin_tpoint_tpoint(const Temporal *temp1, const Temporal *temp2, double dist, bool restr, bool atvalue);
extern Temporal *tintersects_tpoint_geo(const Temporal *temp, const GSERIALIZED *geo, bool restr, bool atvalue);
extern Temporal *ttouches_tpoint_geo(const Temporal *temp, const GSERIALIZED *gs, bool restr, bool atvalue);





extern Temporal *temporal_insert(const Temporal *temp1, const Temporal *temp2, bool connect);
extern Temporal *temporal_update(const Temporal *temp1, const Temporal *temp2, bool connect);
extern Temporal *temporal_delete_timestamp(const Temporal *temp, TimestampTz t, bool connect);
extern Temporal *temporal_delete_timestampset(const Temporal *temp, const Set *ts, bool connect);
extern Temporal *temporal_delete_period(const Temporal *temp, const Span *p, bool connect);
extern Temporal *temporal_delete_periodset(const Temporal *temp, const SpanSet *ps, bool connect);
extern TSequenceSet *temporal_stops(const Temporal *temp, double mindist, const Interval *minduration);





extern SkipList *tbool_tand_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tbool_tor_transfn(SkipList *state, const Temporal *temp);
extern Span *temporal_extent_transfn(Span *p, const Temporal *temp);
extern Temporal *temporal_tagg_finalfn(SkipList *state);
extern SkipList *temporal_tcount_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tfloat_tmax_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tfloat_tmin_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tfloat_tsum_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tint_tmax_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tint_tmin_transfn(SkipList *state, const Temporal *temp);
extern SkipList *tint_tsum_transfn(SkipList *state, const Temporal *temp);
extern double tnumber_integral(const Temporal *temp);
extern TBox *tnumber_extent_transfn(TBox *box, const Temporal *temp);
extern Temporal *tnumber_tavg_finalfn(SkipList *state);
extern SkipList *tnumber_tavg_transfn(SkipList *state, const Temporal *temp);
extern double tnumber_twavg(const Temporal *temp);
extern STBox *tpoint_extent_transfn(STBox *box, const Temporal *temp);
extern GSERIALIZED *tpoint_twcentroid(const Temporal *temp);
extern SkipList *ttext_tmax_transfn(SkipList *state, const Temporal *temp);
extern SkipList *ttext_tmin_transfn(SkipList *state, const Temporal *temp);





extern int int_bucket(int value, int size, int origin);
extern double float_bucket(double value, double size, double origin);
extern TimestampTz timestamptz_bucket(TimestampTz timestamp, const Interval *duration, TimestampTz origin);

extern Span *intspan_bucket_list(const Span *bounds, int size, int origin, int *newcount);
extern Span *floatspan_bucket_list(const Span *bounds, double size, double origin, int *newcount);
extern Span *period_bucket_list(const Span *bounds, const Interval *duration, TimestampTz origin, int *newcount);

extern TBox *tbox_tile_list(const TBox *bounds, double xsize, const Interval *duration, double xorigin, TimestampTz torigin, int *rows, int *columns);

extern Temporal **tint_value_split(Temporal *temp, int size, int origin, int *newcount);
extern Temporal **tfloat_value_split(Temporal *temp, double size, double origin, int *newcount);
extern Temporal **temporal_time_split(Temporal *temp, Interval *duration, TimestampTz torigin, int *newcount);
extern Temporal **tint_value_time_split(Temporal *temp, int size, int vorigin, Interval *duration, TimestampTz torigin, int *newcount);
extern Temporal **tfloat_value_time_split(Temporal *temp, double size, double vorigin, Interval *duration, TimestampTz torigin, int *newcount);

extern STBox *stbox_tile_list(STBox *bounds, double size, const Interval *duration, GSERIALIZED *sorigin, TimestampTz torigin, int **cellcount);





extern double temporal_frechet_distance(const Temporal *temp1, const Temporal *temp2);
extern double temporal_dyntimewarp_distance(const Temporal *temp1, const Temporal *temp2);
extern Match *temporal_frechet_path(const Temporal *temp1, const Temporal *temp2, int *count);
extern Match *temporal_dyntimewarp_path(const Temporal *temp1, const Temporal *temp2, int *count);
extern double temporal_hausdorff_distance(const Temporal *temp1, const Temporal *temp2);





Temporal *geo_to_tpoint(const GSERIALIZED *geo);
Temporal *temporal_simplify_min_dist(const Temporal *temp, double dist);
Temporal *temporal_simplify_min_tdelta(const Temporal *temp, const Interval *mint);
Temporal *temporal_simplify_dp(const Temporal *temp, double eps_dist, bool synchronized);
Temporal *temporal_simplify_max_dist(const Temporal *temp, double eps_dist, bool synchronized);
bool tpoint_AsMVTGeom(const Temporal *temp, const STBox *bounds, int32_t extent,
  int32_t buffer, bool clip_geom, GSERIALIZED **geom, int64 **timesarr, int *count);
bool tpoint_to_geo_measure(const Temporal *tpoint, const Temporal *measure, bool segmentize, GSERIALIZED **result);



//#endif
