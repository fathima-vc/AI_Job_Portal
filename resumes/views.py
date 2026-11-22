

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .models import Resume
from .ai_service import evaluate_resume

from pypdf import PdfReader


@login_required
def upload_resume(request):

    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')

        if not resume_file:
            messages.error(request, 'Please select a resume.')
            return redirect('upload_resume')

        if not resume_file.name.lower().endswith('.pdf'):
            messages.error(request, 'Only PDF files are allowed.')
            return redirect('upload_resume')

        resume = Resume.objects.create(
            user=request.user,
            resume_file=resume_file
        )

        messages.success(request, 'Resume uploaded successfully!')
        return redirect('upload_resume')

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at')

    return render(request, 'resumes/upload.html', {
        'resumes': resumes
    })


@login_required
def analyze_resume(request, resume_id):

    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    try:
        # Extract text from PDF
        pdf_path = resume.resume_file.path
        reader = PdfReader(pdf_path)

        text = ''

        for page in reader.pages:
            text += page.extract_text() or ''

        # Evaluate resume using the free evaluator
        ai_result = evaluate_resume(text)

        if 'error' in ai_result:
            return HttpResponse(
                ai_result['error'],
                status=400
            )

        # Use the same skills detected by the evaluator
        found_skills = ai_result.get('technical_skills', [])

        # Save extracted resume information
        resume.extracted_text = text
        resume.skills = ', '.join(found_skills)
        resume.save()

        # Display results
        return render(request, 'resumes/analysis.html', {
            'resume': resume,
            'skills': found_skills,
            'total_skills': len(found_skills),
            'ai_result': ai_result
        })

    except Exception as e:

        print("RESUME ANALYSIS ERROR:", str(e))

        return HttpResponse(
            f"<h2>Resume Analysis Error</h2><pre>{e}</pre>",
            status=500
        )
