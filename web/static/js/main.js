// Dosya boyutunu formatla
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// Yükleme çubuğunu göster/gizle
function toggleLoadingSpinner(show) {
    const spinner = $('#loading-spinner');
    if (show) {
        if (spinner.length === 0) {
            $('body').append(`
                <div id="loading-spinner" class="position-fixed top-50 start-50 translate-middle">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Yükleniyor...</span>
                    </div>
                </div>
            `);
        }
    } else {
        spinner.remove();
    }
}

// AJAX istekleri için genel hata yakalama
$(document).ajaxError(function(event, jqXHR, settings, error) {
    showAlert('Bir hata oluştu: ' + error, 'danger');
});

// Dosya sürükle-bırak işlemleri
function initializeDragAndDrop() {
    const dropZone = $('#upload-form');
    
    dropZone.on('dragover', function(e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).addClass('bg-light border-primary');
    });
    
    dropZone.on('dragleave', function(e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).removeClass('bg-light border-primary');
    });
    
    dropZone.on('drop', function(e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).removeClass('bg-light border-primary');
        
        const files = e.originalEvent.dataTransfer.files;
        if (files.length > 0) {
            $('#file')[0].files = files;
            $(this).submit();
        }
    });
}

// Sayfa yüklendiğinde
$(document).ready(function() {
    initializeDragAndDrop();
    
    // Form gönderimlerinde yükleme göstergesi
    $('form').on('submit', function() {
        toggleLoadingSpinner(true);
    });
    
    // AJAX tamamlandığında yükleme göstergesini gizle
    $(document).ajaxComplete(function() {
        toggleLoadingSpinner(false);
    });
    
    // Dosya seçildiğinde otomatik yükleme
    $('#file').on('change', function() {
        if (this.files.length > 0) {
            $('#upload-form').submit();
        }
    });
    
    // Tooltip'leri etkinleştir
    $('[data-bs-toggle="tooltip"]').tooltip();
}); 