from typing import List

from pydantic import BaseModel, Field


class SkillGapItem(BaseModel):
    skill: str
    category: str
    demand_score: float
    supply_score: float
    gap_index: float
    status: str
    demand_delta: str
    supply_signal: str
    confidence: int = Field(ge=0, le=100)
    evidence: str


class EmergingSkill(BaseModel):
    skill: str
    growth: str
    signal: str
    horizon: str
    reason: str


class CourseRecommendation(BaseModel):
    id: str
    title: str
    provider: str
    mode: str
    health_score: int = Field(ge=0, le=100)
    alignment: str
    missing_skills: List[str]
    action: str
    evidence: str


class Opportunity(BaseModel):
    id: str
    title: str
    company: str
    location: str
    skills: List[str]
    match: int = Field(ge=0, le=100)
    stipend: str
    posted: str


class MarketOverview(BaseModel):
    location: str
    last_updated: str
    selected_role: str
    total_postings: int
    active_courses: int
    high_demand_skills: int
    critical_gaps: int
    available_opportunities: int
    market_question: str
    source_note: str
    gaps: List[SkillGapItem]
    emerging_skills: List[EmergingSkill]
    courses: List[CourseRecommendation]
    opportunities: List[Opportunity]


class AnalyzeRequest(BaseModel):
    skills_text: str = Field(min_length=2, max_length=10000)
    target_role: str = Field(min_length=2, max_length=120)


class ProfileAnalysis(BaseModel):
    target_role: str
    extracted_skills: List[str]
    normalized_skills: List[str]
    missing_skills: List[str]
    recommended_skills: List[str]
    match_percent: int = Field(ge=0, le=100)
    confidence: int = Field(ge=0, le=100)
    summary: str
    evidence: List[str]
    courses: List[CourseRecommendation]
    opportunities: List[Opportunity]


class InstituteReviewRequest(BaseModel):
    course_name: str = Field(min_length=2, max_length=160)
    degree_name: str = Field(min_length=2, max_length=160)
    syllabus_skills: str = Field(min_length=2, max_length=10000)
    delivery_mode: str = Field(min_length=2, max_length=80)


class InstituteFix(BaseModel):
    skill: str
    priority: str
    prediction_score: int = Field(ge=0, le=100)
    curriculum_coverage: int = Field(ge=0, le=100)
    demand_score: float
    supply_score: float
    gap_index: float
    horizon: str
    recommendation: str
    confidence: int = Field(ge=0, le=100)
    evidence: str


class InstituteReview(BaseModel):
    course_name: str
    degree_name: str
    delivery_mode: str
    model_name: str
    predicted_horizon: str
    health_score: int = Field(ge=0, le=100)
    coverage_percent: int = Field(ge=0, le=100)
    emerging_gap_count: int
    summary: str
    normalized_skills: List[str]
    missing_skills: List[str]
    fixes: List[InstituteFix]
    evidence: List[str]