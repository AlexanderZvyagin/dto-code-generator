// This is an automatically generated file.


function list_equal<Type> (
    a:Type[],
    b:Type[],
    eq:(a:Type,b:Type)=>boolean
): boolean {
    if(a.length!==b.length)
        return false;
    for(let i=0; i<a.length; i++)
        if(!eq(a[i],b[i]))
            return false;
    return true;
}

function float_equal (a:number, b:number) : boolean {
    if(Number.isNaN(a) && Number.isNaN(b)) return true;
    return a===b;
}

function int_equal (a:number, b:number) : boolean {
    return a===b;
}

function string_equal (a:string, b:string) : boolean {
    return a===b;
}


class UpdaterDoc {

    name : string;
    title : string;
    doc_md : string;
    start : string;
    nargs_min : number;
    nrefs_min : number;

    constructor(
        name_ : string  = "",
        title_ : string  = "",
        doc_md_ : string  = "",
        start_ : string  = "",
        nargs_min_ : number  = -88,
        nrefs_min_ : number  = -88,
    ){
        this.name = name_;
        this.title = title_;
        this.doc_md = doc_md_;
        this.start = start_;
        this.nargs_min = nargs_min_;
        this.nrefs_min = nrefs_min_;
    
    }

}
export function
UpdaterDoc_equal (a: UpdaterDoc, b: UpdaterDoc) : boolean {
    if(!string_equal(a.name,b.name)) return false;
    if(!string_equal(a.title,b.title)) return false;
    if(!string_equal(a.doc_md,b.doc_md)) return false;
    if(!string_equal(a.start,b.start)) return false;
    if(!int_equal(a.nargs_min,b.nargs_min)) return false;
    if(!int_equal(a.nrefs_min,b.nrefs_min)) return false;
    return true;
}

export function
UpdaterDoc_fromJSON (j:any, obj: UpdaterDoc): void {
    obj.name = j["name"];
    obj.title = j["title"];
    obj.doc_md = j["doc_md"];
    obj.start = j["start"];
    obj.nargs_min = j["nargs_min"];
    obj.nrefs_min = j["nrefs_min"];
}
export function
UpdaterDoc_fromJSON_string (jstr:string): UpdaterDoc {
    const j = JSON.parse(jstr);
    const obj = new UpdaterDoc();
    UpdaterDoc_fromJSON(j,obj);
    return obj;
}
export function
UpdaterDoc_to_json(j:object, obj:UpdaterDoc) {
    j["name"] = obj.name;
    j["title"] = obj.title;
    j["doc_md"] = obj.doc_md;
    j["start"] = obj.start;
    j["nargs_min"] = obj.nargs_min;
    j["nrefs_min"] = obj.nrefs_min;
}

export function
UpdaterDoc_from_json(j:object, obj:UpdaterDoc) {
    obj.name = j["name"]
    obj.title = j["title"]
    obj.doc_md = j["doc_md"]
    obj.start = j["start"]
    obj.nargs_min = j["nargs_min"]
    obj.nrefs_min = j["nrefs_min"]
}

export function
UpdaterDoc_to_json_string (self:UpdaterDoc) {
    const j = {};
    UpdaterDoc_to_json(j,self);
    return JSON.stringify(j);
}

export function
UpdaterDoc_from_json_string (jstr:string): UpdaterDoc {
    const j: object = JSON.parse(jstr);
    const obj: UpdaterDoc = new UpdaterDoc();
    UpdaterDoc_from_json(j,obj);
    return obj;
}


class UpdaterDto {

    name : string;
    refs : number[]|undefined;
    args : number[]|undefined;
    start : number|undefined;

    constructor(
        name_ : string  = "",
        refs_ : number[]|undefined  = undefined,
        args_ : number[]|undefined  = undefined,
        start_ : number|undefined  = undefined,
    ){
        this.name = name_;
        this.refs = refs_;
        this.args = args_;
        this.start = start_;
    
    }

}
export function
UpdaterDto_equal (a: UpdaterDto, b: UpdaterDto) : boolean {
    if(!string_equal(a.name,b.name)) return false;
    if(a.refs===undefined && b.refs!==undefined) return false;
    if(a.refs!==undefined && b.refs===undefined) return false;
    if(a.refs!==undefined && b.refs!==undefined)
        if(!list_equal(a.refs!,b.refs!,int_equal)) return false;
    if(a.args===undefined && b.args!==undefined) return false;
    if(a.args!==undefined && b.args===undefined) return false;
    if(a.args!==undefined && b.args!==undefined)
        if(!list_equal(a.args!,b.args!,float_equal)) return false;
    if(a.start===undefined && b.start!==undefined) return false;
    if(a.start!==undefined && b.start===undefined) return false;
    if(a.start!==undefined && b.start!==undefined)
    if(!float_equal(a.start!,b.start!)) return false;
    return true;
}

export function
UpdaterDto_fromJSON (j:any, obj: UpdaterDto): void {
    obj.name = j["name"];
    if("refs" in j)
        obj.refs = j["refs"];
    if("args" in j)
        obj.args = j["args"];
    if("start" in j)
        obj.start = j["start"];
}
export function
UpdaterDto_fromJSON_string (jstr:string): UpdaterDto {
    const j = JSON.parse(jstr);
    const obj = new UpdaterDto();
    UpdaterDto_fromJSON(j,obj);
    return obj;
}
export function
UpdaterDto_to_json(j:object, obj:UpdaterDto) {
    j["name"] = obj.name;
    if( obj.refs !== undefined) {
        j["refs"] = obj.refs;
    }
    if( obj.args !== undefined) {
        j["args"] = obj.args;
    }
    if( obj.start !== undefined) {
        j["start"] = obj.start;
    }
}

export function
UpdaterDto_from_json(j:object, obj:UpdaterDto) {
    obj.name = j["name"]
    if("refs" in j)
        obj.refs = j["refs"] as number[]|undefined;
    else
        obj.refs = undefined;
    if("args" in j)
        obj.args = j["args"] as number[]|undefined;
    else
        obj.args = undefined;
    if("start" in j)
        obj.start = j["start"] as number|undefined;
    else
        obj.start = undefined;
}

export function
UpdaterDto_to_json_string (self:UpdaterDto) {
    const j = {};
    UpdaterDto_to_json(j,self);
    return JSON.stringify(j);
}

export function
UpdaterDto_from_json_string (jstr:string): UpdaterDto {
    const j: object = JSON.parse(jstr);
    const obj: UpdaterDto = new UpdaterDto();
    UpdaterDto_from_json(j,obj);
    return obj;
}


class Updater extends UpdaterDto {

    _equation : number;
    _state : number;

    constructor(
        name : string  = "",
        refs : number[]  = [],
        args : number[]  = [],
        start : number|undefined  = undefined,
    ){
        super(
            name,
            refs,
            args,
            start,
        );
        this._equation = -88;
        this._state = -88;
    
    }

    GetStateNumber (
    ) : number  {
        
        if(this._state<0)
            throw new Error(`Updater ${this.name} has no state.`);
        return this._state;
        
    }

    GetEquationNumber (
    ) : number  {
        
        if(this._equation<0)
            throw new Error(`Updater ${this.name} has no _equation.`);
        return this._equation;
        
    }

    HasState (
    ) : boolean  {
        
        return this.start !== undefined;
        
    }

    GetStart (
    ) : number  {
        
        if( this.start === undefined )
            throw new Error("start");
        return this.start;
        
    }

}
export function
Updater_equal (a: Updater, b: Updater) : boolean {
    if(!UpdaterDto_equal(a,b)) return false;
    return true;
}

export function
Updater_fromJSON (j:any, obj: Updater): void {
    UpdaterDto_fromJSON(j,obj)
}
export function
Updater_fromJSON_string (jstr:string): Updater {
    const j = JSON.parse(jstr);
    const obj = new Updater();
    Updater_fromJSON(j,obj);
    return obj;
}
export function
Updater_to_json(j:object, obj:Updater) {
    UpdaterDto_to_json(j,obj);
}

export function
Updater_from_json(j:object, obj:Updater) {
    UpdaterDto_from_json(j,obj);
}

export function
Updater_to_json_string (self:Updater) {
    const j = {};
    Updater_to_json(j,self);
    return JSON.stringify(j);
}

export function
Updater_from_json_string (jstr:string): Updater {
    const j: object = JSON.parse(jstr);
    const obj: Updater = new Updater();
    Updater_from_json(j,obj);
    return obj;
}


class IndependentGaussian extends Updater {


    constructor(
        refs_ : number[]  = [],
    ){
        super(
            "IndependentGaussian",
            refs_,
            [],
            -88,
        );
    
    }

}
export function
IndependentGaussian_equal (a: IndependentGaussian, b: IndependentGaussian) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
IndependentGaussian_fromJSON (j:any, obj: IndependentGaussian): void {
    Updater_fromJSON(j,obj)
}
export function
IndependentGaussian_fromJSON_string (jstr:string): IndependentGaussian {
    const j = JSON.parse(jstr);
    const obj = new IndependentGaussian();
    IndependentGaussian_fromJSON(j,obj);
    return obj;
}
export function
IndependentGaussian_to_json(j:object, obj:IndependentGaussian) {
    Updater_to_json(j,obj);
}

export function
IndependentGaussian_from_json(j:object, obj:IndependentGaussian) {
    Updater_from_json(j,obj);
}

export function
IndependentGaussian_to_json_string (self:IndependentGaussian) {
    const j = {};
    IndependentGaussian_to_json(j,self);
    return JSON.stringify(j);
}

export function
IndependentGaussian_from_json_string (jstr:string): IndependentGaussian {
    const j: object = JSON.parse(jstr);
    const obj: IndependentGaussian = new IndependentGaussian();
    IndependentGaussian_from_json(j,obj);
    return obj;
}


class CorrelatedGaussian extends Updater {


    constructor(
        correlation : number  = Number.NaN,
        state1 : number  = -88,
        state2 : number  = -88,
    ){
        super(
            "CorrelatedGaussian",
            [state1,state2],
            [correlation],
            -88,
        );
    
    }

}
export function
CorrelatedGaussian_equal (a: CorrelatedGaussian, b: CorrelatedGaussian) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
CorrelatedGaussian_fromJSON (j:any, obj: CorrelatedGaussian): void {
    Updater_fromJSON(j,obj)
}
export function
CorrelatedGaussian_fromJSON_string (jstr:string): CorrelatedGaussian {
    const j = JSON.parse(jstr);
    const obj = new CorrelatedGaussian();
    CorrelatedGaussian_fromJSON(j,obj);
    return obj;
}
export function
CorrelatedGaussian_to_json(j:object, obj:CorrelatedGaussian) {
    Updater_to_json(j,obj);
}

export function
CorrelatedGaussian_from_json(j:object, obj:CorrelatedGaussian) {
    Updater_from_json(j,obj);
}

export function
CorrelatedGaussian_to_json_string (self:CorrelatedGaussian) {
    const j = {};
    CorrelatedGaussian_to_json(j,self);
    return JSON.stringify(j);
}

export function
CorrelatedGaussian_from_json_string (jstr:string): CorrelatedGaussian {
    const j: object = JSON.parse(jstr);
    const obj: CorrelatedGaussian = new CorrelatedGaussian();
    CorrelatedGaussian_from_json(j,obj);
    return obj;
}


class BrownianMotion extends Updater {


    constructor(
        start_ : number  = Number.NaN,
        drift_ : number  = Number.NaN,
        diffusion_ : number  = Number.NaN,
    ){
        super(
            "BrownianMotion",
            [],
            [drift_,diffusion_],
            start_,
        );
    
    }

}
export function
BrownianMotion_equal (a: BrownianMotion, b: BrownianMotion) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
BrownianMotion_fromJSON (j:any, obj: BrownianMotion): void {
    Updater_fromJSON(j,obj)
}
export function
BrownianMotion_fromJSON_string (jstr:string): BrownianMotion {
    const j = JSON.parse(jstr);
    const obj = new BrownianMotion();
    BrownianMotion_fromJSON(j,obj);
    return obj;
}
export function
BrownianMotion_to_json(j:object, obj:BrownianMotion) {
    Updater_to_json(j,obj);
}

export function
BrownianMotion_from_json(j:object, obj:BrownianMotion) {
    Updater_from_json(j,obj);
}

export function
BrownianMotion_to_json_string (self:BrownianMotion) {
    const j = {};
    BrownianMotion_to_json(j,self);
    return JSON.stringify(j);
}

export function
BrownianMotion_from_json_string (jstr:string): BrownianMotion {
    const j: object = JSON.parse(jstr);
    const obj: BrownianMotion = new BrownianMotion();
    BrownianMotion_from_json(j,obj);
    return obj;
}


class BrownianMotionRef extends Updater {


    constructor(
        start_ : number  = Number.NaN,
        drift_ : number  = -88,
        diffusion_ : number  = -88,
    ){
        super(
            "BrownianMotion",
            [drift_,diffusion_],
            [],
            start_,
        );
    
    }

}
export function
BrownianMotionRef_equal (a: BrownianMotionRef, b: BrownianMotionRef) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
BrownianMotionRef_fromJSON (j:any, obj: BrownianMotionRef): void {
    Updater_fromJSON(j,obj)
}
export function
BrownianMotionRef_fromJSON_string (jstr:string): BrownianMotionRef {
    const j = JSON.parse(jstr);
    const obj = new BrownianMotionRef();
    BrownianMotionRef_fromJSON(j,obj);
    return obj;
}
export function
BrownianMotionRef_to_json(j:object, obj:BrownianMotionRef) {
    Updater_to_json(j,obj);
}

export function
BrownianMotionRef_from_json(j:object, obj:BrownianMotionRef) {
    Updater_from_json(j,obj);
}

export function
BrownianMotionRef_to_json_string (self:BrownianMotionRef) {
    const j = {};
    BrownianMotionRef_to_json(j,self);
    return JSON.stringify(j);
}

export function
BrownianMotionRef_from_json_string (jstr:string): BrownianMotionRef {
    const j: object = JSON.parse(jstr);
    const obj: BrownianMotionRef = new BrownianMotionRef();
    BrownianMotionRef_from_json(j,obj);
    return obj;
}


class GeometricalBrownianMotion extends Updater {


    constructor(
        start_ : number  = Number.NaN,
        drift_ : number  = Number.NaN,
        diffusion_ : number  = Number.NaN,
    ){
        super(
            "GeometricalBrownianMotion",
            [],
            [drift_,diffusion_],
            start_,
        );
    
    }

}
export function
GeometricalBrownianMotion_equal (a: GeometricalBrownianMotion, b: GeometricalBrownianMotion) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
GeometricalBrownianMotion_fromJSON (j:any, obj: GeometricalBrownianMotion): void {
    Updater_fromJSON(j,obj)
}
export function
GeometricalBrownianMotion_fromJSON_string (jstr:string): GeometricalBrownianMotion {
    const j = JSON.parse(jstr);
    const obj = new GeometricalBrownianMotion();
    GeometricalBrownianMotion_fromJSON(j,obj);
    return obj;
}
export function
GeometricalBrownianMotion_to_json(j:object, obj:GeometricalBrownianMotion) {
    Updater_to_json(j,obj);
}

export function
GeometricalBrownianMotion_from_json(j:object, obj:GeometricalBrownianMotion) {
    Updater_from_json(j,obj);
}

export function
GeometricalBrownianMotion_to_json_string (self:GeometricalBrownianMotion) {
    const j = {};
    GeometricalBrownianMotion_to_json(j,self);
    return JSON.stringify(j);
}

export function
GeometricalBrownianMotion_from_json_string (jstr:string): GeometricalBrownianMotion {
    const j: object = JSON.parse(jstr);
    const obj: GeometricalBrownianMotion = new GeometricalBrownianMotion();
    GeometricalBrownianMotion_from_json(j,obj);
    return obj;
}


class GeometricalBrownianMotionRef extends Updater {


    constructor(
        start_ : number  = Number.NaN,
        drift_ : number  = -88,
        diffusion_ : number  = -88,
    ){
        super(
            "GeometricalBrownianMotion",
            [drift_,diffusion_],
            [],
            start_,
        );
    
    }

}
export function
GeometricalBrownianMotionRef_equal (a: GeometricalBrownianMotionRef, b: GeometricalBrownianMotionRef) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
GeometricalBrownianMotionRef_fromJSON (j:any, obj: GeometricalBrownianMotionRef): void {
    Updater_fromJSON(j,obj)
}
export function
GeometricalBrownianMotionRef_fromJSON_string (jstr:string): GeometricalBrownianMotionRef {
    const j = JSON.parse(jstr);
    const obj = new GeometricalBrownianMotionRef();
    GeometricalBrownianMotionRef_fromJSON(j,obj);
    return obj;
}
export function
GeometricalBrownianMotionRef_to_json(j:object, obj:GeometricalBrownianMotionRef) {
    Updater_to_json(j,obj);
}

export function
GeometricalBrownianMotionRef_from_json(j:object, obj:GeometricalBrownianMotionRef) {
    Updater_from_json(j,obj);
}

export function
GeometricalBrownianMotionRef_to_json_string (self:GeometricalBrownianMotionRef) {
    const j = {};
    GeometricalBrownianMotionRef_to_json(j,self);
    return JSON.stringify(j);
}

export function
GeometricalBrownianMotionRef_from_json_string (jstr:string): GeometricalBrownianMotionRef {
    const j: object = JSON.parse(jstr);
    const obj: GeometricalBrownianMotionRef = new GeometricalBrownianMotionRef();
    GeometricalBrownianMotionRef_from_json(j,obj);
    return obj;
}


class ZeroCouponBond extends Updater {


    constructor(
        underlying_ : number  = -88,
        start_ : number  = Number.NaN,
    ){
        super(
            "ZeroCouponBond",
            [underlying_],
            [],
            start_,
        );
    
    }

}
export function
ZeroCouponBond_equal (a: ZeroCouponBond, b: ZeroCouponBond) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
ZeroCouponBond_fromJSON (j:any, obj: ZeroCouponBond): void {
    Updater_fromJSON(j,obj)
}
export function
ZeroCouponBond_fromJSON_string (jstr:string): ZeroCouponBond {
    const j = JSON.parse(jstr);
    const obj = new ZeroCouponBond();
    ZeroCouponBond_fromJSON(j,obj);
    return obj;
}
export function
ZeroCouponBond_to_json(j:object, obj:ZeroCouponBond) {
    Updater_to_json(j,obj);
}

export function
ZeroCouponBond_from_json(j:object, obj:ZeroCouponBond) {
    Updater_from_json(j,obj);
}

export function
ZeroCouponBond_to_json_string (self:ZeroCouponBond) {
    const j = {};
    ZeroCouponBond_to_json(j,self);
    return JSON.stringify(j);
}

export function
ZeroCouponBond_from_json_string (jstr:string): ZeroCouponBond {
    const j: object = JSON.parse(jstr);
    const obj: ZeroCouponBond = new ZeroCouponBond();
    ZeroCouponBond_from_json(j,obj);
    return obj;
}


class Option extends Updater {


    constructor(
        underlying_ : number  = -88,
        strike_ : number  = Number.NaN,
        call_put_ : number  = -88,
    ){
        super(
            "Option",
            [underlying_],
            [strike_,call_put_],
            undefined,
        );
    
    }

}
export function
Option_equal (a: Option, b: Option) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
Option_fromJSON (j:any, obj: Option): void {
    Updater_fromJSON(j,obj)
}
export function
Option_fromJSON_string (jstr:string): Option {
    const j = JSON.parse(jstr);
    const obj = new Option();
    Option_fromJSON(j,obj);
    return obj;
}
export function
Option_to_json(j:object, obj:Option) {
    Updater_to_json(j,obj);
}

export function
Option_from_json(j:object, obj:Option) {
    Updater_from_json(j,obj);
}

export function
Option_to_json_string (self:Option) {
    const j = {};
    Option_to_json(j,self);
    return JSON.stringify(j);
}

export function
Option_from_json_string (jstr:string): Option {
    const j: object = JSON.parse(jstr);
    const obj: Option = new Option();
    Option_from_json(j,obj);
    return obj;
}


class Barrier extends Updater {


    constructor(
        underlying : number  = -88,
        start : number  = Number.NaN,
        level : number  = Number.NaN,
        direction : number  = -88,
        action : number  = -88,
        value : number  = Number.NaN,
    ){
        super(
            "Barrier",
            [underlying],
            [level,value,direction,action],
            start,
        );
    
    }

}
export function
Barrier_equal (a: Barrier, b: Barrier) : boolean {
    if(!Updater_equal(a,b)) return false;
    return true;
}

export function
Barrier_fromJSON (j:any, obj: Barrier): void {
    Updater_fromJSON(j,obj)
}
export function
Barrier_fromJSON_string (jstr:string): Barrier {
    const j = JSON.parse(jstr);
    const obj = new Barrier();
    Barrier_fromJSON(j,obj);
    return obj;
}
export function
Barrier_to_json(j:object, obj:Barrier) {
    Updater_to_json(j,obj);
}

export function
Barrier_from_json(j:object, obj:Barrier) {
    Updater_from_json(j,obj);
}

export function
Barrier_to_json_string (self:Barrier) {
    const j = {};
    Barrier_to_json(j,self);
    return JSON.stringify(j);
}

export function
Barrier_from_json_string (jstr:string): Barrier {
    const j: object = JSON.parse(jstr);
    const obj: Barrier = new Barrier();
    Barrier_from_json(j,obj);
    return obj;
}


class HistogramAxis {

    state : number;
    nbins : number;
    min : number;
    max : number;

    constructor(
        _state : number  = -88,
        _nbins : number  = -88,
        _min : number  = -88,
        _max : number  = -88,
    ){
        this.state = _state;
        this.nbins = _nbins;
        this.min = _min;
        this.max = _max;
    
    }

}
export function
HistogramAxis_equal (a: HistogramAxis, b: HistogramAxis) : boolean {
    if(!int_equal(a.state,b.state)) return false;
    if(!int_equal(a.nbins,b.nbins)) return false;
    if(!float_equal(a.min,b.min)) return false;
    if(!float_equal(a.max,b.max)) return false;
    return true;
}

export function
HistogramAxis_fromJSON (j:any, obj: HistogramAxis): void {
    obj.state = j["state"];
    obj.nbins = j["nbins"];
    obj.min = j["min"];
    obj.max = j["max"];
}
export function
HistogramAxis_fromJSON_string (jstr:string): HistogramAxis {
    const j = JSON.parse(jstr);
    const obj = new HistogramAxis();
    HistogramAxis_fromJSON(j,obj);
    return obj;
}
export function
HistogramAxis_to_json(j:object, obj:HistogramAxis) {
    j["state"] = obj.state;
    j["nbins"] = obj.nbins;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

export function
HistogramAxis_from_json(j:object, obj:HistogramAxis) {
    obj.state = j["state"]
    obj.nbins = j["nbins"]
    obj.min = j["min"]
    obj.max = j["max"]
}

export function
HistogramAxis_to_json_string (self:HistogramAxis) {
    const j = {};
    HistogramAxis_to_json(j,self);
    return JSON.stringify(j);
}

export function
HistogramAxis_from_json_string (jstr:string): HistogramAxis {
    const j: object = JSON.parse(jstr);
    const obj: HistogramAxis = new HistogramAxis();
    HistogramAxis_from_json(j,obj);
    return obj;
}


class Histogram {

    x : HistogramAxis;
    y : HistogramAxis|undefined;

    constructor(
        x : HistogramAxis  = new HistogramAxis(),
        y : HistogramAxis|undefined  = undefined,
    ){
        this.x = x;
        this.y = y;
    
    }

}
export function
Histogram_equal (a: Histogram, b: Histogram) : boolean {
    if(!HistogramAxis_equal(a.x,b.x)) return false;
    if(a.y===undefined && b.y!==undefined) return false;
    if(a.y!==undefined && b.y===undefined) return false;
    if(a.y!==undefined && b.y!==undefined)
    if(!HistogramAxis_equal(a.y!,b.y!)) return false;
    return true;
}

export function
Histogram_fromJSON (j:any, obj: Histogram): void {
    obj.x = j["x"];
    if("y" in j)
        obj.y = j["y"];
}
export function
Histogram_fromJSON_string (jstr:string): Histogram {
    const j = JSON.parse(jstr);
    const obj = new Histogram();
    Histogram_fromJSON(j,obj);
    return obj;
}
export function
Histogram_to_json(j:object, obj:Histogram) {
    {
        const jj = {};
        HistogramAxis_to_json(jj,obj.x);
        j["x"] = jj;
    }
    if( obj.y !== undefined) {
        {
            const jj = {};
            HistogramAxis_to_json(jj,obj.y);
            j["y"] = jj;
        }
    }
}

export function
Histogram_from_json(j:object, obj:Histogram) {
    HistogramAxis_from_json(j["x"],obj.x);
    if( "y" in j)
        obj.y = j["y"] as HistogramAxis|undefined;
}

export function
Histogram_to_json_string (self:Histogram) {
    const j = {};
    Histogram_to_json(j,self);
    return JSON.stringify(j);
}

export function
Histogram_from_json_string (jstr:string): Histogram {
    const j: object = JSON.parse(jstr);
    const obj: Histogram = new Histogram();
    Histogram_from_json(j,obj);
    return obj;
}


class EvaluationPoint {

    state : number;
    time : number;
    value : number|undefined;
    error : number|undefined;
    histograms : Histogram[];

    constructor(
        state_ : number  = -88,
        time_ : number  = Number.NaN,
        value_ : number|undefined  = undefined,
        error_ : number|undefined  = undefined,
        histograms_ : Histogram[]  = [],
    ){
        this.state = state_;
        this.time = time_;
        this.value = value_;
        this.error = error_;
        this.histograms = histograms_;
    
    }

    GetState (
    ) : number  {
        
        return this.state;
        
    }

    GetTime (
    ) : number  {
        
        return this.time;
        
    }

    GetValue (
    ) : number  {
        
        if( this.value === undefined )
            throw new Error("value");
        return this.value;
        
    }

    GetError (
    ) : number  {
        
        if( this.error === undefined )
            throw new Error("error");
        return this.error;
        
    }

    Add (
        
        histogram : Histogram,
    ) : EvaluationPoint  {
        
        this.histograms.push(histogram);
        return this;
        
    }

}
export function
EvaluationPoint_equal (a: EvaluationPoint, b: EvaluationPoint) : boolean {
    if(!int_equal(a.state,b.state)) return false;
    if(!float_equal(a.time,b.time)) return false;
    if(a.value===undefined && b.value!==undefined) return false;
    if(a.value!==undefined && b.value===undefined) return false;
    if(a.value!==undefined && b.value!==undefined)
    if(!float_equal(a.value!,b.value!)) return false;
    if(a.error===undefined && b.error!==undefined) return false;
    if(a.error!==undefined && b.error===undefined) return false;
    if(a.error!==undefined && b.error!==undefined)
    if(!float_equal(a.error!,b.error!)) return false;
    if(!list_equal(a.histograms,b.histograms,Histogram_equal)) return false;
    return true;
}

export function
EvaluationPoint_fromJSON (j:any, obj: EvaluationPoint): void {
    obj.state = j["state"];
    obj.time = j["time"];
    if("value" in j)
        obj.value = j["value"];
    if("error" in j)
        obj.error = j["error"];
    obj.histograms = j["histograms"];
}
export function
EvaluationPoint_fromJSON_string (jstr:string): EvaluationPoint {
    const j = JSON.parse(jstr);
    const obj = new EvaluationPoint();
    EvaluationPoint_fromJSON(j,obj);
    return obj;
}
export function
EvaluationPoint_to_json(j:object, obj:EvaluationPoint) {
    j["state"] = obj.state;
    j["time"] = obj.time;
    if( obj.value !== undefined) {
        j["value"] = obj.value;
    }
    if( obj.error !== undefined) {
        j["error"] = obj.error;
    }
    j["histograms"] = [];
    for(let item of obj.histograms) {
        const jj = {};
        Histogram_to_json(jj,item);
        j["histograms"].push(jj);
    }
}

export function
EvaluationPoint_from_json(j:object, obj:EvaluationPoint) {
    obj.state = j["state"]
    obj.time = j["time"]
    if("value" in j)
        obj.value = j["value"] as number|undefined;
    else
        obj.value = undefined;
    if("error" in j)
        obj.error = j["error"] as number|undefined;
    else
        obj.error = undefined;
    for(let item of j["histograms"]) {
        const v: Histogram = new Histogram();
        Histogram_from_json(item,v);
        obj.histograms.push(v);
    }
}

export function
EvaluationPoint_to_json_string (self:EvaluationPoint) {
    const j = {};
    EvaluationPoint_to_json(j,self);
    return JSON.stringify(j);
}

export function
EvaluationPoint_from_json_string (jstr:string): EvaluationPoint {
    const j: object = JSON.parse(jstr);
    const obj: EvaluationPoint = new EvaluationPoint();
    EvaluationPoint_from_json(j,obj);
    return obj;
}


class Parameter {

    value : number;
    step : number;
    min : number;
    max : number;

    constructor(
        value_ : number  = Number.NaN,
        step_ : number  = Number.NaN,
        min_ : number  = Number.NaN,
        max_ : number  = Number.NaN,
    ){
        this.value = value_;
        this.step = step_;
        this.min = min_;
        this.max = max_;
    
    }

}
export function
Parameter_equal (a: Parameter, b: Parameter) : boolean {
    if(!float_equal(a.value,b.value)) return false;
    if(!float_equal(a.step,b.step)) return false;
    if(!float_equal(a.min,b.min)) return false;
    if(!float_equal(a.max,b.max)) return false;
    return true;
}

export function
Parameter_fromJSON (j:any, obj: Parameter): void {
    obj.value = j["value"];
    obj.step = j["step"];
    obj.min = j["min"];
    obj.max = j["max"];
}
export function
Parameter_fromJSON_string (jstr:string): Parameter {
    const j = JSON.parse(jstr);
    const obj = new Parameter();
    Parameter_fromJSON(j,obj);
    return obj;
}
export function
Parameter_to_json(j:object, obj:Parameter) {
    j["value"] = obj.value;
    j["step"] = obj.step;
    j["min"] = obj.min;
    j["max"] = obj.max;
}

export function
Parameter_from_json(j:object, obj:Parameter) {
    obj.value = j["value"]
    obj.step = j["step"]
    obj.min = j["min"]
    obj.max = j["max"]
}

export function
Parameter_to_json_string (self:Parameter) {
    const j = {};
    Parameter_to_json(j,self);
    return JSON.stringify(j);
}

export function
Parameter_from_json_string (jstr:string): Parameter {
    const j: object = JSON.parse(jstr);
    const obj: Parameter = new Parameter();
    Parameter_from_json(j,obj);
    return obj;
}


class Model {

    TimeStart : number;
    TimeSteps : number;
    NumPaths : number;
    updaters : Updater[];
    evaluations : EvaluationPoint[];
    RunTimeoutSeconds : number;
    MemoryLimitKB : number;

    constructor(
        TimeStart_ : number  = Number.NaN,
        TimeSteps_ : number  = 0,
        NumPaths_ : number  = 0,
        updaters_ : Updater[]  = [],
        evaluations_ : EvaluationPoint[]  = [],
        RunTimeoutSeconds_ : number  = 1,
        MemoryLimitKB_ : number  = 1,
    ){
        this.TimeStart = TimeStart_;
        this.TimeSteps = TimeSteps_;
        this.NumPaths = NumPaths_;
        this.updaters = updaters_;
        this.evaluations = evaluations_;
        this.RunTimeoutSeconds = RunTimeoutSeconds_;
        this.MemoryLimitKB = MemoryLimitKB_;
    
    }

    GetNumberOfUpdaters (
    ) : number  {
        
        return this.updaters.length;
        
    }

    GetNumberOfStates (
    ) : number  {
        
        return this.updaters.filter(
            u => u.HasState()
        ).length;
        
    }

    Add (
        
        updater : Updater,
    ) : Updater  {
        
        this.updaters.push(updater);
        updater._equation = this.GetNumberOfUpdaters()-1;
        if(updater.HasState())
            updater._state = this.GetNumberOfStates()-1;
        return updater;
        
    }

}
export function
Model_equal (a: Model, b: Model) : boolean {
    if(!float_equal(a.TimeStart,b.TimeStart)) return false;
    if(!int_equal(a.TimeSteps,b.TimeSteps)) return false;
    if(!int_equal(a.NumPaths,b.NumPaths)) return false;
    if(!list_equal(a.updaters,b.updaters,Updater_equal)) return false;
    if(!list_equal(a.evaluations,b.evaluations,EvaluationPoint_equal)) return false;
    if(!float_equal(a.RunTimeoutSeconds,b.RunTimeoutSeconds)) return false;
    if(!int_equal(a.MemoryLimitKB,b.MemoryLimitKB)) return false;
    return true;
}

export function
Model_fromJSON (j:any, obj: Model): void {
    obj.TimeStart = j["TimeStart"];
    obj.TimeSteps = j["TimeSteps"];
    obj.NumPaths = j["NumPaths"];
    obj.updaters = j["updaters"];
    obj.evaluations = j["evaluations"];
    obj.RunTimeoutSeconds = j["RunTimeoutSeconds"];
    obj.MemoryLimitKB = j["MemoryLimitKB"];
}
export function
Model_fromJSON_string (jstr:string): Model {
    const j = JSON.parse(jstr);
    const obj = new Model();
    Model_fromJSON(j,obj);
    return obj;
}
export function
Model_to_json(j:object, obj:Model) {
    j["TimeStart"] = obj.TimeStart;
    j["TimeSteps"] = obj.TimeSteps;
    j["NumPaths"] = obj.NumPaths;
    j["updaters"] = [];
    for(let item of obj.updaters) {
        const jj = {};
        Updater_to_json(jj,item);
        j["updaters"].push(jj);
    }
    j["evaluations"] = [];
    for(let item of obj.evaluations) {
        const jj = {};
        EvaluationPoint_to_json(jj,item);
        j["evaluations"].push(jj);
    }
    j["RunTimeoutSeconds"] = obj.RunTimeoutSeconds;
    j["MemoryLimitKB"] = obj.MemoryLimitKB;
}

export function
Model_from_json(j:object, obj:Model) {
    obj.TimeStart = j["TimeStart"]
    obj.TimeSteps = j["TimeSteps"]
    obj.NumPaths = j["NumPaths"]
    for(let item of j["updaters"]) {
        const v: Updater = new Updater();
        Updater_from_json(item,v);
        obj.updaters.push(v);
    }
    for(let item of j["evaluations"]) {
        const v: EvaluationPoint = new EvaluationPoint();
        EvaluationPoint_from_json(item,v);
        obj.evaluations.push(v);
    }
    obj.RunTimeoutSeconds = j["RunTimeoutSeconds"]
    obj.MemoryLimitKB = j["MemoryLimitKB"]
}

export function
Model_to_json_string (self:Model) {
    const j = {};
    Model_to_json(j,self);
    return JSON.stringify(j);
}

export function
Model_from_json_string (jstr:string): Model {
    const j: object = JSON.parse(jstr);
    const obj: Model = new Model();
    Model_from_json(j,obj);
    return obj;
}


class EvaluationResults {

    names : string[];
    npaths : number[];
    mean : number[];
    stddev : number[];
    skewness : number[];
    time_points : number[];
    time_steps : number[];
    histograms : Histogram[];
    model : Model|undefined;

    constructor(
        names_ : string[]  = [],
        npaths_ : number[]  = [],
        mean_ : number[]  = [],
        stddev_ : number[]  = [],
        skewness_ : number[]  = [],
        time_points_ : number[]  = [],
        time_steps_ : number[]  = [],
        histograms_ : Histogram[]  = [],
        model_ : Model|undefined  = undefined,
    ){
        this.names = names_;
        this.npaths = npaths_;
        this.mean = mean_;
        this.stddev = stddev_;
        this.skewness = skewness_;
        this.time_points = time_points_;
        this.time_steps = time_steps_;
        this.histograms = histograms_;
        this.model = model_;
    
    }

}
export function
EvaluationResults_equal (a: EvaluationResults, b: EvaluationResults) : boolean {
    if(!list_equal(a.names,b.names,string_equal)) return false;
    if(!list_equal(a.npaths,b.npaths,int_equal)) return false;
    if(!list_equal(a.mean,b.mean,float_equal)) return false;
    if(!list_equal(a.stddev,b.stddev,float_equal)) return false;
    if(!list_equal(a.skewness,b.skewness,float_equal)) return false;
    if(!list_equal(a.time_points,b.time_points,float_equal)) return false;
    if(!list_equal(a.time_steps,b.time_steps,int_equal)) return false;
    if(!list_equal(a.histograms,b.histograms,Histogram_equal)) return false;
    if(a.model===undefined && b.model!==undefined) return false;
    if(a.model!==undefined && b.model===undefined) return false;
    if(a.model!==undefined && b.model!==undefined)
    if(!Model_equal(a.model!,b.model!)) return false;
    return true;
}

export function
EvaluationResults_fromJSON (j:any, obj: EvaluationResults): void {
    obj.names = j["names"];
    obj.npaths = j["npaths"];
    obj.mean = j["mean"];
    obj.stddev = j["stddev"];
    obj.skewness = j["skewness"];
    obj.time_points = j["time_points"];
    obj.time_steps = j["time_steps"];
    obj.histograms = j["histograms"];
    if("model" in j)
        obj.model = j["model"];
}
export function
EvaluationResults_fromJSON_string (jstr:string): EvaluationResults {
    const j = JSON.parse(jstr);
    const obj = new EvaluationResults();
    EvaluationResults_fromJSON(j,obj);
    return obj;
}
export function
EvaluationResults_to_json(j:object, obj:EvaluationResults) {
    j["names"] = obj.names;
    j["npaths"] = obj.npaths;
    j["mean"] = obj.mean;
    j["stddev"] = obj.stddev;
    j["skewness"] = obj.skewness;
    j["time_points"] = obj.time_points;
    j["time_steps"] = obj.time_steps;
    j["histograms"] = [];
    for(let item of obj.histograms) {
        const jj = {};
        Histogram_to_json(jj,item);
        j["histograms"].push(jj);
    }
    if( obj.model !== undefined) {
        {
            const jj = {};
            Model_to_json(jj,obj.model);
            j["model"] = jj;
        }
    }
}

export function
EvaluationResults_from_json(j:object, obj:EvaluationResults) {
    obj.names = j["names"]
    obj.npaths = j["npaths"]
    obj.mean = j["mean"]
    obj.stddev = j["stddev"]
    obj.skewness = j["skewness"]
    obj.time_points = j["time_points"]
    obj.time_steps = j["time_steps"]
    for(let item of j["histograms"]) {
        const v: Histogram = new Histogram();
        Histogram_from_json(item,v);
        obj.histograms.push(v);
    }
    if( "model" in j)
        obj.model = j["model"] as Model|undefined;
}

export function
EvaluationResults_to_json_string (self:EvaluationResults) {
    const j = {};
    EvaluationResults_to_json(j,self);
    return JSON.stringify(j);
}

export function
EvaluationResults_from_json_string (jstr:string): EvaluationResults {
    const j: object = JSON.parse(jstr);
    const obj: EvaluationResults = new EvaluationResults();
    EvaluationResults_from_json(j,obj);
    return obj;
}


export {
    UpdaterDoc,
    UpdaterDto,
    Updater,
    IndependentGaussian,
    CorrelatedGaussian,
    BrownianMotion,
    BrownianMotionRef,
    GeometricalBrownianMotion,
    GeometricalBrownianMotionRef,
    ZeroCouponBond,
    Option,
    Barrier,
    HistogramAxis,
    Histogram,
    EvaluationPoint,
    Parameter,
    Model,
    EvaluationResults,
}
