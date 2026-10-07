<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('maintenances', function (Blueprint $table) {
            $table->id();
            $table->foreignId('alat_id')->constrained()->cascadeOnDelete();
            $table->date('tanggal');
            $table->string('jenis_maintenance');
            $table->text('deskripsi')->nullable();
            $table->decimal('biaya', 15, 2)->nullable();
            $table->enum('status', ['Direncanakan', 'Sedang Proses', 'Selesai']);
            $table->date('tanggal_selesai')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('maintenances');
    }
};
